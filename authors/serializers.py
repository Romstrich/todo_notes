from rest_framework.serializers import ModelSerializer

from .models import Author

class AuthorModelSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Author