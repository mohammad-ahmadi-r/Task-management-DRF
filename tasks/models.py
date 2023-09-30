from django.db import models
from like.models import Like
from django.contrib.contenttypes.fields import GenericRelation


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Like, related_query_name='task')

    def __str__(self):
        return self.title
