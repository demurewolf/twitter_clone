from django.http import Http404
from django.shortcuts import render, redirect

from .models import Quote, Comment
from .forms import QuoteForm, CommentForm

from users.models import Follow

from django.contrib.auth.decorators import login_required


# Home page of quoter app
def index(request):
    if request.user.is_authenticated:
        following = Follow.objects.filter(src_user=request.user).values('dst_user')
        feed = Quote.objects.filter(author__in=following).order_by('-pub_date')
    else:
        feed = Quote.objects.order_by('-pub_date')

    return render(request, 'quotes/index.html', context={'quotes': feed})


def quote_detail(request, quote_id):
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
        delete_perm = request.user.username == quote.author.username

    else:
        form = None
        delete_perm = False

    comments = Comment.objects.filter(quote=quote_id)

    return render(request, 'quotes/detail.html',
                  context={'quote': quote, 'comments': comments, 'form': form, 'delete_perm': delete_perm})


@login_required(login_url="login")
def create_quote(request):
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
def delete_quote(request, quote_id):
    Quote.objects.filter(id=quote_id, author=request.user).delete()
    return index(request)  # Redirect to homepage


@login_required(login_url="login")
def requote(request, quote_id):
    return Http404("Coming underway")


@login_required(login_url="login")
def delete_requote(request, quote_id):
    return Http404("coming underway")
