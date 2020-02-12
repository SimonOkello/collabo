from django.shortcuts import render
from django.http import HttpResponse
from . import views
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def login(request):
    return render(request, 'login.html', {})


def profile(request):
    return render(request, 'profile.html', {})


def project(request):
    return render(request, 'project.html', {})


def detail(request):
    return render(request, 'portfolio-detail.html', {})


def review(request):
    return render(request, 'review.html', {})


