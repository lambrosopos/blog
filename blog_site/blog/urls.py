from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post_index, name='post_index'),
]
