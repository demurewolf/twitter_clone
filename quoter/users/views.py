from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, ProfileForm
from .models import Profile, Follow

from quotes.models import Quote


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for %s" % username)
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', context={'form': form})


@login_required(login_url="login")
def follow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    user_following = request.user

    if not Follow.objects.filter(src_user=user_following, dst_user=user_to_follow):
        new_follow = Follow(src_user=user_following, dst_user=user_to_follow)
        new_follow.save()

    return HttpResponse("noOp")


@login_required(login_url="login")
def unfollow_user(request, username):
    user_to_follow = get_object_or_404(User, username=username)
    user_following = request.user

    Follow.objects.filter(src_user=user_following, dst_user=user_to_follow).delete()
    return HttpResponse("noOp")


def followers(request, username):
    user = get_object_or_404(User, username=username)
    followers = Follow.objects.filter(dst_user=user)
    followers_names = [f.src_user for f in followers]

    return render(request, 'users/follow_list.html',
                  context={'names': followers_names, 'follow_template_name': 'users/followers.html'})


def following(request, username):
    user = get_object_or_404(User, username=username)
    following = Follow.objects.filter(src_user=user)
    following_names = [f.dst_user for f in following]

    return render(request, 'users/follow_list.html',
                  context={'names': following_names, 'follow_template_name': 'users/following.html'})


def profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    can_edit = request.user.is_authenticated and (request.user.username == username)

    try:
        profile = Profile.objects.get(user=profile_user)
    except Profile.DoesNotExist:
        profile = Profile()

    followers_count = Follow.objects.filter(dst_user=profile_user).count()
    following_count = Follow.objects.filter(src_user=profile_user).count()

    _context = {
        'can_edit': can_edit,
        'profile_username': profile_user.username,
        'info': profile.get_fields,
        'followers': followers_count,
        'following': following_count,
    }

    return render(request, 'users/profile.html', context=_context)


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
    search_term = ''
    if 'search_query' in request.GET:
        search_term = request.GET['search_query']
        users = [u.username for u in User.objects.filter(username__icontains=search_term)]
        placeholder_text = search_term

    else:
        users = []
        placeholder_text = "Enter your query..."

    return render(request, 'users/search.html', context={'results': users, 'placeholder': placeholder_text})
