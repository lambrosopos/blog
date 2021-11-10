import uuid
from django.db import models

class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=128)
    post_body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __repr__(self):
        return f"Post <{self.uuid}>"


class Tags(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)

    def __repr__(self):
        return f"Tag <{self.uuid}>" 
