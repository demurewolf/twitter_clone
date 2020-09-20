from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxLengthValidator
from django.contrib.auth.models import User

# Create your models here.
class Quote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=400, validators=[MaxLengthValidator(400)])
    pub_date = models.DateTimeField(default=now)
    
    @property
    def comment_count(self):
        return Comment.objects.filter(author=self.author)

    @property
    def requote_count(self):
        return Requote.objects.filter(author=self.author)

    def __str__(self):
        return self.content[:20]
     
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=400, validators=[MaxLengthValidator(400)])
    pub_date = models.DateTimeField(default=now)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)

class Requote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=now)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)