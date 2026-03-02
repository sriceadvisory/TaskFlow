from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializer import TasksSerializer
from .models import Tasks

# Create your views here.
class TasksListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

    #Filtering and searching settings
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["title"]
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['-created_at']

class TasksDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer

