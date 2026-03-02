from django.urls import path
from .views import TasksListCreateAPIView, TasksDetailAPIView

urlpatterns = [
    path("", TasksListCreateAPIView.as_view(),name="index"),
    path("<int:pk>/", TasksDetailAPIView.as_view(),name="tasks_detail_views"),
]