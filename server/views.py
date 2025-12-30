from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, ProfileSerializer, TaskSerializer
from .models import Task

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class ProfileView(RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class TaskView(RetrieveAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)