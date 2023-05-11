from rest_framework.serializers import ModelSerializer
from posts.models import Post
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name
        token['username'] = user.username

        return token

class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']



class PostSerializers(ModelSerializer):
    # author = UserSerializers()
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'created', 'updated']
        # depth = 1

    