from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    bio = models.CharField(max_length=250)
    

    # following
    # followers
    # pub_quotes
    # likes
    # re_quotes
