from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Tag

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

class PostIndexListView(ListView):
    model               = Post
    template_name       = 'blog/post/post_index.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.all()
        return context


class PostItemDetailView(DetailView):
    model               = Post
    template_name       = 'blog/post/post_view.html'
    context_object_name = 'post'


def search_results(request):
    return render(request, 'blog/search_results.html')