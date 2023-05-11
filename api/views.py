from django.shortcuts import render
from api.serializers import *
from posts.models import *  
from rest_framework.views import APIView, Response
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import *
from rest_framework import viewsets
# Create your views here.

# class PostListView(APIView):

#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializers(posts, many = True)
#         return Response(serializer.data)
#     def post(self, request, format=None):
#         serializer = PostSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializers



# Shu narsa generic view bilan qilingani

# class PostListAPIView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly,]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

# class PostCreateAPIView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthorOrReadOnly,]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

# class PostDeleteAPIView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers

# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers