from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from users.serializers import UserModelSerializer
from .models import Project,Todo

class ProjectModelSerialiser(ModelSerializer):
    # users=StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = '__all__'

class TodoModelSerialiser(ModelSerializer):
    class Meta:
        model = Todo
        fields='__all__'