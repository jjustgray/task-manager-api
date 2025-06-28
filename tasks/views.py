from rest_framework import viewsets, permissions, generics
from .models import Task, CustomUser
from .serializers import TaskSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated

import redis
from rest_framework.decorators import api_view
from rest_framework.response import Response

# 🔧 Ініціалізація Redis-клієнта (має бути зверху)
redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0)

@api_view(['GET'])
def online_users_view(request):
    users = redis_client.smembers("online_users")
    usernames = [u.decode('utf-8') for u in users]
    return Response({"online_users": usernames})


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
