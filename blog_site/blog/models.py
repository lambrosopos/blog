import uuid
from django.db import models
from django.forms import ModelForm

class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __repr__(self):
        return f"Post <{self.uuid}>"


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'body']


class Tag(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)

    def __repr__(self):
        return f"Tag <{self.uuid}>" 


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
