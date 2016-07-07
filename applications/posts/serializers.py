from rest_framework import serializers
from .models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "post_name", "post_content", "post_tags", "post_created", "post_edited", "post_published")
