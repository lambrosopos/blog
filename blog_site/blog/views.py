from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def post_index(request):
    return render(request, 'blog/post/post_index.html')
