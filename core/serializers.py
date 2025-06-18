from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'role', 'assigned_dispatcher')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            role=validated_data['role'],
            assigned_dispatcher=validated_data.get('assigned_dispatcher')
        )
        return user

class TaskSerializer(serializers.ModelSerializer):
    worker_name = serializers.ReadOnlyField(source='worker.username')

    class Meta:
        model = Task
        fields = '__all__'
