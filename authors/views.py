from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer

from .models import Author, Biography, Book
from .serializers import AuthorModelSerializer, BiographyModelSerializer, BookModelSerializer


class AuthorModelViewSet(ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

class BiographyModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer

class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer