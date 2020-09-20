from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'quotes/index.html')

def detail(request, quote_id):
    return render(request, 'quotes/detail.html', context={'quote_id': quote_id})

def create(request):
    return render(request, 'quotes/create.html')

def delete(request, quote_id):
    return render(request, 'quotes/delete.html', context={'quote_id': quote_id})

