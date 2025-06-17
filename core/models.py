from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('worker', 'Worker'),
        ('dispatcher', 'Dispatcher'),
        ('supervisor', 'Supervisor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    assigned_dispatcher = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='workers')

class Task(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'worker'})
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.worker.username} - {self.start_time} to {self.end_time or 'In progress'}"