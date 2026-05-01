from django.contrib.auth.models import User
from blog.models import Post

def post_create(*, author: User, title: str, content: str) -> Post:
    post = Post(author=author, title=title, content=content)
    post.full_clean()
    post.save()
    return post

def post_update(*, post: Post, title: str = None, content: str = None) -> Post:
    if title is not None:
        post.title = title
    if content is not None:
        post.content = content
    
    post.full_clean()
    post.save()
    return post

def post_delete(*, post: Post):
    post.delete()
