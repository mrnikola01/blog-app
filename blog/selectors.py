from django.db.models import QuerySet
from blog.models import Post

def post_list() -> QuerySet[Post]:
    return Post.objects.all().order_by('-created_at')

def post_get(post_id: int) -> Post:
    return Post.objects.get(id=post_id)
