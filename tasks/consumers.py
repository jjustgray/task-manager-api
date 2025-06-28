import json
from channels.generic.websocket import AsyncWebsocketConsumer
import redis

# ініціалізація Redis
redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0)

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'tasks_room'

        # Отримуємо username з query string, наприклад ?username=user1
        self.username = self.scope["query_string"].decode("utf-8").replace("username=", "") or "anonymous"

        # Додаємо до групи
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

        # Зберігаємо як онлайн
        redis_client.sadd("online_users", self.username)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

        # Видаляємо з Redis
        redis_client.srem("online_users", self.username)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'task_message',
                'message': data['message'],
            }
        )

    async def task_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))
