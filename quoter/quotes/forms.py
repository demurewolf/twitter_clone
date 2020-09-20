
from django.forms import ModelForm

from .models import Quote, Comment, Requote

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['content']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
