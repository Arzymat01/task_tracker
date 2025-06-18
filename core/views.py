# core/views.py

from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import RegisterSerializer, TaskSerializer
from .models import Task
from .permissions import IsWorker, IsDispatcher, IsSupervisor
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone

User = get_user_model()

# Каттоо (регистрация)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# Логин (JWT)
class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


# Жумушчу: баштоо
class StartTaskView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsWorker]

    def post(self, request):
        task = Task.objects.create(worker=request.user)
        return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)


# Жумушчу: бүтүрүү
class EndTaskView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsWorker]

    def post(self, request):
        task = Task.objects.filter(worker=request.user, end_time__isnull=True).last()
        if task:
            task.end_time = timezone.now()
            task.is_completed = True
            task.save()
            return Response(TaskSerializer(task).data)
        return Response({"detail": "Активдүү тапшырма жок."}, status=400)


# Диспетчер: өз жумушчуларынын тапшырмалары
class DispatcherWorkerTasksView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsDispatcher]

    def get(self, request):
        workers = User.objects.filter(assigned_dispatcher=request.user)
        tasks = Task.objects.filter(worker__in=workers)
        return Response(TaskSerializer(tasks, many=True).data)


# Супервайзер: бардык тапшырмаларды көрүү
class AllTasksView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsSupervisor]

    def get(self, request):
        tasks = Task.objects.all()
        return Response(TaskSerializer(tasks, many=True).data)
