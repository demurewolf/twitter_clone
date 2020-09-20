from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 

from .forms import RegisterForm

# Create your views here.
def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for %s" % username)
            return redirect('/')

    else:
        form = RegisterForm()
    
    return render(request, 'registration/register.html', context={'form': form})

def profile(request, username):
    return render(request, 'users/profile.html', context={'username': username})

def followers(request, username):
    return render(request, 'users/followers.html', context={'username': username})

def following(request, username):
    return render(request, 'users/following.html', context={'username': username})