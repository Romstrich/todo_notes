from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserModelSerializer


# class UserModelViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer

# Отобразить список user
class UserListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

class UserRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

class UserUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
