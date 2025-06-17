from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'role', 'assigned_dispatcher')

class TaskSerializer(serializers.ModelSerializer):
    worker_name = serializers.ReadOnlyField(source='worker.username')

    class Meta:
        model = Task
        fields = '__all__'