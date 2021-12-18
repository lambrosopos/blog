from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.PostIndexListView.as_view(), name='post_index'),
    path('posts/<int:pk>', views.PostItemDetailView.as_view(), name='post_view'),
    path('search', views.search_results, name='search'),
]
