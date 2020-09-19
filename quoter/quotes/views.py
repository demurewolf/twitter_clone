from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Index page.")

def detail(request, quote_id):
    return HttpResponse("Quote page for quote id %s" % quote_id)
