from django.http import Http404
from django.shortcuts import render, redirect

from .models import Quote, Comment
from .forms import QuoteForm, CommentForm

from django.contrib.auth.decorators import login_required

# Home page of quoter app
def index(request):
    feed = Quote.objects.order_by('-pub_date')
    return render(request, 'quotes/index.html', context={'quotes': feed})

def detail(request, quote_id):
    try:
        quote = Quote.objects.get(pk=quote_id)
    except Quote.DoesNotExist:
        raise Http404("Quote does note exist!")

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.quote = quote
            form.save()

    # Present form for new comments if user is logged in
    if request.user.is_authenticated:
        form = CommentForm()
    else:
        form = None
        
    comments = Comment.objects.filter(quote=quote_id)

    return render(request, 'quotes/detail.html', context={'quote': quote, 'comments': comments, 'form': form})

@login_required
def create(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/')
    
    else:
        form = QuoteForm()

    return render(request, 'quotes/create.html', context={'form': form})

@login_required(login_url="login")
def delete(request, quote_id):
    Quote.objects.filter(id=quote_id, author=request.user).delete()
    return index(request) # Redirect to homepage
    
@login_required
def requote(request, quote_id):
    return Http404("Coming underway")