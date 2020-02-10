from django.shortcuts import render
from django.http import HttpResponse
from . import views
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def detail(request):
    return render(request, 'portfolio-detail.html', {})

def signup(request):
    return HttpResponse("This is signup page")

def login(request):
    return HttpResponse("This is login page")

