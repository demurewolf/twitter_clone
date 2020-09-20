from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import RegisterForm

# Create your views here.

def profile(request, username):
    return render(request, 'users/profile.html', context={'username': username})

def login(request):
    return render(request, 'users/login.html')

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', context={'form': form})