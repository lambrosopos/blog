from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.PostIndexListView.as_view(), name='post_index'),
    path('post/create', views.post_create, name='post_create'),
    path('post/<int:pk>', views.PostItemDetailView.as_view(), name='post_view'),
    path('post/<post_id>/edit', views.post_edit, name='post_edit'),
]
