from django.shortcuts import render, get_object_or_404
from .forms import RegisterForm
from .models import Project, Category
from django.views.generic import ListView, DetailView
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
