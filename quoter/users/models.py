from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    nickname = models.CharField(max_length=30, blank=True)
    bio = models.CharField(max_length=350, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    @property
    def followers(self):
        return Follow.objects.filter(user=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(follower=self.user).count()

    def __str__(self):
        return "%s's user profile." % self.user.username


class Follow(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    # likes
    # re_quotes
