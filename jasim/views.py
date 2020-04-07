from django.shortcuts import render, get_object_or_404,redirect
from .forms import RegisterForm, LoginForm
from .models import Project, Category
from django.views.generic import ListView, DetailView
from django.contrib.auth import login as auth_login, authenticate
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           user=form.save()
           auth_login(request, user)
           return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    form_class = LoginForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
                    
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(
                username, password))
                return HttpResponse("Invalid login details given")
        
    return render(request, 'login.html', {'form': form})



def profile(request):

    return render(request, 'profile.html', {})


def category(request, **kwargs):
    context = {}
    context['category_projects'] = Project.objects.filter(
        category_id=kwargs.get('pk'))
    context['cat_lists'] = Category.objects.all()

    return render(request, 'category.html', context)


def project(request):
    context = {}
    context['projects_lists'] = Project.objects.all().order_by('-created_on')
    context['cat_lists'] = Category.objects.all()

    return render(request, 'project.html', context)


class ProjectDetail(DetailView):
    model = Project
    template_name = 'project-detail.html'


def review(request):
    return render(request, 'review.html', {})
