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

    def __str__(self):
        return "%s's user profile." % self.user.get_username()
