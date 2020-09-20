from django.http import HttpResponse
from django.shortcuts import render

# from djgano.views import generic

# Create your views here.

def profile(request, username):
    return render(request, 'users/profile.html', context={'username': username})

def login(request):
    return render(request, 'users/login.html')

def register(request):
    return render(request, 'users/register.html')