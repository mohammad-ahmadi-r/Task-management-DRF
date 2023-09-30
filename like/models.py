from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres import indexes as psql_indexes
from django.db import models
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from like.managers import LikeManager


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='temporary')
    object_id = models.PositiveIntegerField()
    target = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = LikeManager()

    # class Meta:
    #     ordering = ['-created_at']
    #     get_latest_by = 'created_at'
    #     unique_together = ('user', 'content_type', 'object_id')
    #     verbose_name = 'like'
    #     verbose_name_plural = 'likes'

    def __str__(self):
        return u'{} liked {}'.format(self.user, self.target)
