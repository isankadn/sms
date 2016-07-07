from django.db import models


class Post(models.Model):
    post_name = models.CharField(max_length=100)
    post_content = models.TextField(max_length=500)
    post_tags = models.CharField(max_length=100)
    post_created = models.DateTimeField(auto_now=True)
    post_edited = models.DateTimeField(auto_now_add=True)
    post_published = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.post_name
