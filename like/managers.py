from typing import Union, Dict

from django.contrib.contenttypes.models import ContentType
from django.db import models, transaction


class LikeManager(models.Manager):
    @transaction.atomic
    def is_liked(self, user, instance) -> bool:
        """
        Check if the object is liked or not.
        :param instance:
        :param user:
        :return bool:
        """
        if not user.is_authenticated:
            return False

        content_type = ContentType.objects.get_for_model(instance)
        return self.model.objects.filter(user=user, content_type=content_type, object_id=instance.pk).cache().exists()

    @transaction.atomic
    def like(self, user, instance, manage_like_count=False) -> Dict[str, Union[str, str]]:
        """
        Check if the object was liked or not, if not, it will be add to the likes
        else it will be remove from the likes table.
        it returns the proper message based on the situation.

        :param user:
        :param instance:
        :param manage_like_count:
        :return:
        """
        print('in the like')
        like, liked = self.get_or_create(user=user, content_type=ContentType.objects.get_for_model(instance),
                                         object_id=instance.pk)
        print(like)

        if not liked:
            like.delete()

        if manage_like_count:
            if not liked:
                print('not liked')
                # instance.__class__.objects.decrease_likes_count(instance)
            else:
                print('liked')
                # instance.__class__.objects.increase_likes_count(instance)

        return {"is_liked": liked, "message": "Liked" if liked else "Disliked"}

    def get_liked_object_ids(self, user, **kwargs) -> list:
        """
        It returns list of liked object ids, the result
        is sorted based on the creation date.
        :param user:
        :param kwargs:
        :return list:
        """
        return self.filter(user=user, **kwargs).values_list('object_id', flat=True)

    def get_instance_likes_count(self, instance) -> int:
        """
        It returns count of likes for the passed instance
        :param instance:
        :return int:
        """
        return self.filter(content_type=ContentType.objects.get_for_model(instance), object_id=instance.pk).count()
