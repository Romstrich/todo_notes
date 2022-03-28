from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer\
    , StringRelatedField

from .models import Author,Biography,Book

class AuthorModelSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Author

class BiographyModelSerializer(ModelSerializer):
    author=AuthorModelSerializer()
    class Meta:
        model = Biography
        fields = '__all__'


class BookModelSerializer(ModelSerializer):
    authors=StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = '__all__'
