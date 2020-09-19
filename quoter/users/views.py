from django.http import HttpResponse
from django.shortcuts import render

# from djgano.views import generic

# Create your views here.

def profile(request, username):
    return HttpResponse("found the profile for user: %s" % username)