from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .import models as m


def index(request):
    return render(request, 'blog/index.html')


class PostIndexListView(ListView):
    model               = m.Post
    template_name       = 'blog/post/post_index.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_list'] = m.Tag.objects.all()
        return context


class PostItemDetailView(DetailView):
    model               = m.Post
    template_name       = 'blog/post/post_view.html'
    context_object_name = 'post'


def search_results(request):
    search_term = request.GET.get('q', '').strip()

    context = {}

    if search_term:
        query_results = m.Post.objects.filter(title__icontains=search_term)
        context['posts'] = [_ for _ in query_results]


    return render(request, 'blog/search_results.html', context=context)
