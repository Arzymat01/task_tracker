from django.urls import path
from .views import (
    RegisterView, LoginView, StartTaskView, EndTaskView,
    DispatcherWorkerTasksView, AllTasksView
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),

    path('start-task/', StartTaskView.as_view()),
    path('end-task/', EndTaskView.as_view()),
    path('dispatcher-tasks/', DispatcherWorkerTasksView.as_view()),
    path('all-tasks/', AllTasksView.as_view()),
]
