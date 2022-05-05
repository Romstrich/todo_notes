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

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields='__all__'


class Query(ObjectType):

    all_todo=List(TodoType)
    all_project=List(ProjectType)
    all_users=List(UserType)

    def resolve_all_todo(root,info):
        return Todo.objects.all()

    def resolve_all_project(root,info):
        return Project.objects.all()

    def resolve_all_users(root,info):
        return User.objects.all()

schema = Schema(query=Query)