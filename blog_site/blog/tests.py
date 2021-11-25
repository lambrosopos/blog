from django.test import TestCase
from blog.models import Post, Tag

class PostTestCase(TestCase):
    def setUp(self):
        self.test_post_1 = {
            "title":"Test Post title",
            "subtitle":"Test Post Subtitle",
            "body":"#Header 1"
        }

        Post.objects.create(
            title=self.test_post_1.title,
            subtitle=self.test_post_1.subtitle,
            body=self.test_post_1.body
        )

    def test_post_has_appropriate_properties(self):
        test_post = Post.objects.get(
            title=self.test_post_1.title,
            subtitle=self.test_post_1.subtitle,
            body=self.test_post_1.body
        )
        self.assertIsNotNone(test_post.uuid)
        self.assertIsNotNone(test_post.created_at)
        self.assertIsNotNone(test_post.updated_at)

