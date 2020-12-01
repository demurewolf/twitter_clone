from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, ProfileForm
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
    profile_user = get_object_or_404(User, username=username)
    can_edit = request.user.is_authenticated and (request.user.username == username)

    try:
        profile = Profile.objects.get(user=profile_user)
    except Profile.DoesNotExist:
        profile = Profile()

    return render(request, 'users/profile.html', context={'can_edit': can_edit, 'profile_username': profile_user.username,'info': profile.get_fields})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            
            username = request.user.username
            messages.success(request, "Account created for %s" % username)
            
            return redirect('users:profile', username=username)

    else:
        form = ProfileForm()

    return render(request, 'users/edit_profile.html', context={'form': form})

def search(request):
    return HttpResponse("coming underway...")