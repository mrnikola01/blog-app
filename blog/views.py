from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from blog.models import Post
from blog.serializers import PostSerializer, RegisterSerializer
from blog.selectors import post_list, post_get
from blog.services import post_create, post_update, post_delete
from blog.permissions import IsAuthorOrReadOnly

class RegisterApi(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class PostListApi(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = post_list()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        post_create(
            author=request.user,
            title=serializer.validated_data['title'],
            content=serializer.validated_data['content']
        )
        
        return Response(status=status.HTTP_201_CREATED)

class PostDetailApi(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get(self, request, post_id):
        try:
            post = post_get(post_id=post_id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, post_id):
        try:
            post = post_get(post_id=post_id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        self.check_object_permissions(request, post)
        
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        post_update(
            post=post,
            title=serializer.validated_data.get('title'),
            content=serializer.validated_data.get('content')
        )
        
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, post_id):
        try:
            post = post_get(post_id=post_id)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        self.check_object_permissions(request, post)
        
        post_delete(post=post)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
