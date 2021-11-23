import uuid
from django.db import models


class Tag(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __repr__(self):
        return f"Tag <{self.uuid}>"


class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __repr__(self):
        return f"Post <{self.uuid}>"
