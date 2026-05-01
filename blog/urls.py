from django.urls import path
from blog.views import PostListApi, PostDetailApi, RegisterApi

urlpatterns = [
    path('register/', RegisterApi.as_view(), name='register'),
    path('posts/', PostListApi.as_view(), name='post_list'),
    path('posts/<int:post_id>/', PostDetailApi.as_view(), name='post_detail'),
]
