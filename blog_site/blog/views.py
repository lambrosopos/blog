from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post/post_index.html'

def post_view(request, post_id):
    return render(request, 'blog/post/post_view.html')

def post_create(request):
    return render(request, 'blog/post/post_create.html')

def post_edit(request, post_id):
    return render(request, 'blog/post/post_edit.html')
