import io


from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from test_models import Author

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()

    def __str__(self):
        return str(self.name)+' '+str(self.birthday_year)

    def create(self, validated_data):
        return Author(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday_year = validated_data.get('birthday_year',instance.birthday_year)
        return instance

def start():
    data = {'name': 'Грин', 'birthday_year': 1880}
    serializer = AuthorSerializer(data=data)
    serializer.is_valid()
    author = serializer.save()
    print(author)

    data = {'name': 'Александр', 'birthday_year': 1880}
    serializer = AuthorSerializer(author, data=data)
    serializer.is_valid()
    author = serializer.save()
    print(author)

    data = {'birthday_year': 2000}
    serializer = AuthorSerializer(author, data=data, partial=True)
    serializer.is_valid()
    author = serializer.save()
    print(author)

start()