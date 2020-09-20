from django.contrib import admin

# Register your models here.
from .models import Quote, Comment, Requote

admin.site.register(Quote)
admin.site.register(Comment)
admin.site.register(Requote)