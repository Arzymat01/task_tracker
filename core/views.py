from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from django.utils import timezone

from .models import Task, User
from .serializers import TaskSerializer, UserSerializer
from .permissions import IsWorker, IsDispatcher, IsSupervisor


# Жумуш баштоо — Worker гана
class StartTaskView(APIView):
    permission_classes = [IsAuthenticated, IsWorker]

    def post(self, request):
        task = Task.objects.create(worker=request.user)
        return Response(TaskSerializer(task).data)


# Жумушту аяктоо — Worker гана
class EndTaskView(APIView):
    permission_classes = [IsAuthenticated, IsWorker]

    def post(self, request):
        try:
            task = Task.objects.filter(worker=request.user, is_completed=False).latest('start_time')
            task.end_time = timezone.now()
            task.is_completed = True
            task.save()
            return Response(TaskSerializer(task).data)
        except Task.DoesNotExist:
            return Response({"error": "Активдүү жумуш табылган жок."}, status=404)


# Диспетчер өз жумушчуларынын бардык жумуштарын көрөт
class DispatcherWorkerTasksView(APIView):
    permission_classes = [IsAuthenticated, IsDispatcher]

    def get(self, request):
        workers = User.objects.filter(assigned_dispatcher=request.user)
        tasks = Task.objects.filter(worker__in=workers).order_by('-start_time')
        return Response(TaskSerializer(tasks, many=True).data)


# Супервайзер бардык жумуштарды көрөт
class AllTasksView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsSupervisor]
    queryset = Task.objects.all().order_by('-start_time')
    serializer_class = TaskSerializer


# Өзү жөнүндө маалымат алуу
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)
