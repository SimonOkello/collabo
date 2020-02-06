from django.shortcuts import render
from django.http import HttpResponse
from . import views
# Create your views here.

def index(request):
    return HttpResponse("This is landing page")

def signup(request):
    return HttpResponse("This is signup page")

def login(request):
    return HttpResponse("This is login page")

