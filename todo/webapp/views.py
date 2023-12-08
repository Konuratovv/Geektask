from rest_framework import viewsets

from webapp.models import Task
from webapp.serializer import TaskSerializer


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
