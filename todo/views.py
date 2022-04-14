from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from todo.models import Project, Todo
from todo.serializers import ProjectModelSerialiser, TodoModelSerialiser


class ProjectModelViewSet(ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectModelSerialiser

class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerialiser

