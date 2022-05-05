# import graphene
from graphene import ObjectType, Schema, String, List
from graphene_django import DjangoObjectType
from todo.models import Todo, Project
from users.models import User


# class Querry(ObjectType):
#     hello=String(default_value='HI, MAN!')

class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(ObjectType):

    all_todo=List(TodoType)
    all_project=List(ProjectType)

    def resolve_all_todo(root,info):
        return Todo.objects.all()

    def resolve_all_project(root,info):
        return Project.objects.all()


schema = Schema(query=Query)
