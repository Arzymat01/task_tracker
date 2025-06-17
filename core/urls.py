from django.urls import path
from . import views

urlpatterns = [
    path('start-task/', views.StartTaskView.as_view()),
    path('end-task/', views.EndTaskView.as_view()),
    path('dispatcher-tasks/', views.DispatcherWorkerTasksView.as_view()),
    path('all-tasks/', views.AllTasksView.as_view()),
]