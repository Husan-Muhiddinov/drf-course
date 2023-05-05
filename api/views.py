from django.shortcuts import render
from .serializers import *
from posts.models import *  
from rest_framework.views import APIView, Response
# Create your views here.

class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many = True)
        return Response(serializer.data)