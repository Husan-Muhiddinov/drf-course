from rest_framework.serializers import ModelSerializer
from posts.models import Post
from django.contrib.auth.models import User

class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']



class PostSerializers(ModelSerializer):
    author = UserSerializers
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'created', 'updated']
        depth = 1