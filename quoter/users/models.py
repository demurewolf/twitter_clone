from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)

    nickname = models.CharField(max_length=30, blank=True)
    bio = models.CharField(max_length=350, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    @property
    def get_fields(self):
        return [
            ('nickname', self.nickname),
            ('bio', self.bio),
            ('location', self.location),
            ('birth_date', self.birth_date),
        ]

    @property
    def follower_count(self):
        return Follow.objects.filter(dst_user=self.user).count()

    def __str__(self):
        return "%s's user profile." % self.user.username


class Follow(models.Model):
    # User making the follow request
    src_user = models.ForeignKey(User, related_name='sources', on_delete=models.CASCADE)

    # User requested to follow
    dst_user = models.ForeignKey(User, related_name='destinations', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('src_user', 'dst_user'),)
