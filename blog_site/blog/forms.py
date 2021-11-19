from django.forms import ModelForm
from .models import Post, Tag

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'body']

