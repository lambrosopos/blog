from dataclasses import dataclass

from django.urls import resolve
from django.test import TestCase, RequestFactory
from blog.models import Post
from blog.views import (index,
                        PostIndexListView,
                        PostItemDetailView,
                        search_results)


class IndexPageTest(TestCase):
    def test_root_url_resolves_to_index_page(self):
        found = resolve('/')
        self.assertEqual(found.func, index)


class PostIndexPageTest(TestCase):
    def setUp(self):
        self.url_path = '/posts'
        self.factory = RequestFactory()

    def test_root_post_url_resolves_to_post_index_page(self):
        found = resolve(self.url_path)
        self.assertEqual(found.func.__name__,
                         PostIndexListView.as_view().__name__)

    def test_post_index_page_returns_correct_html(self):
        request = self.factory.get(self.url_path)
        response = PostIndexListView.as_view()(request)

        html = response.render().content.decode('utf8')
        self.assertTrue(html.startswith('\n<!DOCTYPE html>'))
        self.assertIn('Introduction', html)
        self.assertIn('Welcome to posts index page', html)


class PostItemPageTest(TestCase):
    fixtures = ["post_fixtures.json"]

    def setUp(self):
        self.url_path = '/posts/1'
        self.factory = RequestFactory()

    def test_post_detail_url_resolves_to_post_detail_page(self):
        found = resolve(self.url_path)
        self.assertEqual(found.func.__name__, 
                         PostItemDetailView.as_view().__name__)

    def test_post_detail_page_shows_correct_post_item(self):
        request = self.factory.get(self.url_path)
        response = PostItemDetailView.as_view()(request, pk=1)

        html = response.render().content.decode('utf8')
        self.assertTrue(html.startswith('\n<!DOCTYPE html>'))



class SearchPageTest(TestCase):
    def test_search_url_resolves_to_search_page(self):
        found = resolve('/search')
        self.assertEqual(found.func, search_results)
