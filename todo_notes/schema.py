#import graphene
from graphene import ObjectType, Schema, String
from graphene_django import DjangoObjectType
from todo.models import Todo,Project
from users.models import User



class Querry(ObjectType):
    hello=String(default_value='HI, MAN!')

schema=Schema(query=Querry)