from django.urls import resolve
from django.test import TestCase
from blog.views import index, PostIndexListView, PostItemDetailView


class IndexPageTest(TestCase):
    def test_root_url_resolves_to_index_page(self):
        found = resolve('/')
        self.assertEqual(found.func, index)


class PostPageTest(TestCase):
    def test_root_post_url_resolves_to_post_index_page(self):
        found = resolve('/posts')
        self.assertEqual(found.func.__name__,
                         PostIndexListView.as_view().__name__)

    def test_post_detail_url_resolves_to_post_detail_page(self):
        found = resolve('/posts/1')
        self.assertEqual(found.func.__name__, 
                         PostItemDetailView.as_view().__name__)


