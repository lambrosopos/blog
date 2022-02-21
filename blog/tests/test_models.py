from datetime import date

from django.test import TestCase
from blog.models import Post, Tag
from .tests import predefined_dataclasses as pred_dc

class PostTestCase(TestCase):
    fixtures = ["post_fixtures.json"]

    def setUp(self):
        self.test_post_1 = pred_dc.PostDataClass(
            title      = "Test Post Title",
            subtitle   = "Test Post Subtitle",
            body       = "#Header 1",
            created_at = date(2021, 1, 1),
            updated_at = date(2021, 1, 1)
        )

        self.test_post_2 = pred_dc.PostDataClass(
            title      = "Test Post Title 2",
            subtitle   = "Test Post Subtitle 2",
            body       = "#Header 1",
            created_at = date(2021, 1, 2),
            updated_at = date(2021, 1, 3)
        )

    def test_post_1_has_appropriate_properties(self):
        test_post = Post.objects.get(
            title    = self.test_post_1.title,
            subtitle = self.test_post_1.subtitle,
            body     = self.test_post_1.body,
        )

        self.assertIsNotNone(test_post.uuid)
        self.assertEqual(test_post.title, self.test_post_1.title)
        self.assertEqual(test_post.subtitle, self.test_post_1.subtitle)
        self.assertEqual(test_post.body, self.test_post_1.body)
        self.assertEqual(test_post.created_at,
                         self.test_post_1.created_at)
        self.assertEqual(test_post.updated_at,
                         self.test_post_1.updated_at)

    def test_post_2_has_appropriate_properties(self):
        test_post = Post.objects.get(
            title    = self.test_post_2.title,
            subtitle = self.test_post_2.subtitle,
            body     = self.test_post_2.body,
        )

        self.assertIsNotNone(test_post.uuid)
        self.assertEqual(test_post.title, self.test_post_2.title)
        self.assertEqual(test_post.subtitle, self.test_post_2.subtitle)
        self.assertEqual(test_post.body, self.test_post_2.body)
        self.assertEqual(test_post.created_at,
                         self.test_post_2.created_at)
        self.assertEqual(test_post.updated_at,
                         self.test_post_2.updated_at)


class TagTestCase(TestCase):
    def setUp(self):
        self.test_tag_1 = pred_dc.TagDataClass(
            name='test_tag'
        )

        Tag.objects.create(
            name = self.test_tag_1.name
        )

    def test_tag_has_appropriate_properties(self):
        test_tag = Tag.objects.get(
            name = self.test_tag_1.name
        )

        self.assertEqual(test_tag.name, self.test_tag_1.name)
        self.assertIsNotNone(test_tag.uuid)

