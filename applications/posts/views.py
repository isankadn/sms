from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-post_created")
    serializer_class = PostSerializers
