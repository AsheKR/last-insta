from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    img_profile = models.ImageField(
        upload_to="user"
    )
    relation_users = models.ManyToManyField(
        'self',
        symmetrical=False,
    )
    mention = models.ForeignKey(
        'posts.Comment',
        on_delete=models.CASCADE,
    )


class UserRelation(models.Model):
    CHOICE_BLOCK_OR_FOLLOW = {
        ('f', 'Follow'),
        ('b', 'Block'),
    }

    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='to_user_relations',
        related_query_name='to_user_relation',
    )
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='from_user_relations',
        related_query_name='from_user_relation',
    )
    relation_type = models.CharField(
        max_length=1,
        choices=CHOICE_BLOCK_OR_FOLLOW,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('to_user', 'from_user'),
        )