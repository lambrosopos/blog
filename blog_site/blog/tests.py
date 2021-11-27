from dataclasses import dataclass

from django.test import TestCase
from blog.models import Post, Tag

class PostTestCase(TestCase):
    def setUp(self):
        # Set up Post Data Class
        @dataclass
        class PostDataClass:
            title   : str
            subtitle: str
            body    : str

        self.test_post_1 = PostDataClass(
            title    = "Test Post Title",
            subtitle = "Test Post Subtitle",
            body     = "#Header 1"
        )

        Post.objects.create(
            title    = self.test_post_1.title,
            subtitle = self.test_post_1.subtitle,
            body     = self.test_post_1.body,
        )

    def test_post_has_appropriate_properties(self):
        test_post = Post.objects.get(
            title    = self.test_post_1.title,
            subtitle = self.test_post_1.subtitle,
            body     = self.test_post_1.body,
        )

        self.assertEqual(test_post.title, self.test_post_1.title)
        self.assertEqual(test_post.subtitle, self.test_post_1.subtitle)
        self.assertEqual(test_post.body, self.test_post_1.body)
        self.assertIsNotNone(test_post.uuid)
        self.assertIsNotNone(test_post.created_at)
        self.assertIsNotNone(test_post.updated_at)


class TagTestCase(TestCase):
    def setUp(self):
        @dataclass
        class TagDataClass:
            name: str

        self.test_tag_1 = TagDataClass(
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
