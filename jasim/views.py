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

def category(request, category_id):
    categories = Category.objects.all()
    projects = Project.objects.all().order_by('-created_on')
    category = get_object_or_404(Category, pk = category_id)
    projects = projects.filter(category=category)
    return render(request, 'category.html', {'categories':categories, 'projects': projects, 'category':category})

class ProjectList(ListView):
    queryset = Project.objects.all().order_by('-created_on')
    template_name = 'project.html'


class ProjectDetail(DetailView):
    model = Project
    template_name = 'project-detail.html'


def review(request):
    return render(request, 'review.html', {})
