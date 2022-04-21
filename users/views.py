from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet

from .models import User
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

# Отобразить список user
# class UserListAPIView(ListAPIView):
#     renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#
# class UserRetrieveAPIView(RetrieveAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#
# class UserUpdateAPIView(UpdateAPIView):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer

# class UserViewSet(ViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#
#     def list(self,request):
#         user=User.objects.all()
#         serializer_class = UserModelSerializer(user,many=True)
#         return Response(serializer_class.data)
#
#     def retrieve(self,request,pk=None):
#         user=get_object_or_404(User,pk=pk)
#         serializer_class = UserModelSerializer(user)
#         return Response(serializer_class.data)
#
#     def update(self,request,pk=None):
#         user=get_object_or_404(User,pk=pk)
#         serializer_class = UserModelSerializer(user)
#         return Response(serializer_class.data)

# class UserModelViewSet(ModelViewSet):
#     renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer

class UserCustomViewSet(ListModelMixin,UpdateModelMixin,RetrieveAPIView,GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer