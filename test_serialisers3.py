from collections import OrderedDict

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from test_models import Author, Biography, Article, Book


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()

class BiographySerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1024)
    author = AuthorSerializer()

class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    authors = AuthorSerializer(many=True)

class ArticleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    author = AuthorSerializer()

def start():
    author1 = Author('Грин', 1880)
    serializer = AuthorSerializer(author1)
    print(serializer.data)

    biography = Biography('Текст биографии', author1)
    serializer = BiographySerializer(biography)
    print(serializer.data)

    article = Article('Некоторая статья', author1)
    serializer = ArticleSerializer(article)
    print(serializer.data) #

    author2 = Author('Пушкин', 1799)
    book = Book('Некоторая книга', [author1, author2])
    serializer = BookSerializer(book)
    print(serializer.data)

start()