from django.db import models

# Create your models here.
class Quote(models.Model):
    content = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    requotes = models.IntegerField(default=0)
    
    #  images = models.ImageField()
    # replies
     
