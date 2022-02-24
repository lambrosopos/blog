from datetime import date

from django.urls import resolve
from django.test import TestCase, RequestFactory

from blog.models import Post
from blog.views import (index,
                        PostIndexListView,
                        PostItemDetailView,
                        search_results)
from . import predefined_dataclasses as pred_dc


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


class SearchFunctionTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.test_post_1 = pred_dc.PostDataClass(
            title      = "Dolphin's Rainbow",
            subtitle   = "Gladly Rejoin Cafe",
            body       = "#2 Dolphins Reunite",
            created_at = date(2021, 1, 1),
            updated_at = date(2021, 1, 1)
        )

    def test_search_returns_correct_results(self):
        request = self.factory.get('/search?q=Dolphin')
        response = search_results(request)

        html = response.render().html.decode('utf8')
        self.assertTrue(html.startswith('\n<!DOCTYPE html>'))
