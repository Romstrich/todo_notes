from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.mixins import UpdateModelMixin, ListModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from todo.filters import TodoFilter
from todo.models import Project, Todo
from todo.serializers import ProjectModelSerialiser, TodoModelSerialiser

class ProjectLimitPagination(LimitOffsetPagination):
    default_limit=10

class TodoLimitPagination(LimitOffsetPagination):
    default_limit=20


class ProjectCustomViewSet(ListAPIView,CreateModelMixin,DestroyModelMixin,UpdateModelMixin,GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerialiser

class TodoCustomViewSet(ListAPIView,CreateModelMixin,DestroyModelMixin,UpdateModelMixin,GenericViewSet):
    #renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerialiser
    filterset_class=TodoFilter
    pagination_class = TodoLimitPagination


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerialiser
    pagination_class = ProjectLimitPagination

    def get_queryset(self):
        name=self.request.query_params.get('name','')
        projects=Project.objects.all()
        if name:
            projects=projects.filter(name__contains=name)
        return projects

# class TodoDjangoFilterViewSet(ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoModelSerialiser
#     filterset_fields=['project']

