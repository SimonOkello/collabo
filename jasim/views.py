from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    return render(request, 'login.html', {})


def detail(request):
    return render(request, 'project-detail.html', {})


def profile(request):
    return render(request, 'profile.html', {})


def project(request):
    return render(request, 'project.html', {})


def review(request):
    return render(request, 'review.html', {})


