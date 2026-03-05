from django.urls import path
from .views import TasksListCreateAPIView, TasksDetailAPIView

urlpatterns = [
    path("tasks/", TasksListCreateAPIView.as_view(), name="tasks_list_create"),
    path("tasks/<int:pk>/", TasksDetailAPIView.as_view(), name="tasks_detail"),
]