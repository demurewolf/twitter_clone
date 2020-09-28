from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User

from .forms import RegisterForm
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for %s" % username)
            return redirect('registration/login/')

    else:
        form = RegisterForm()
    
    return render(request, 'registration/register.html', context={'form': form})

def profile(request, username):
    user = get_object_or_404(User, username=username)

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile()

    return render(request, 'users/profile.html', context={'user': user, 'profile': Profile.Meta.get_fields()})

def followers(request, username):
    return render(request, 'users/followers.html', context={'username': username})

def following(request, username):
    return render(request, 'users/following.html', context={'username': username})

def search(request):
    return HttpResponse("coming underway...")