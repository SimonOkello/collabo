from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('category/<int:pk>/', views.category, name = 'category'),
    path('project/', views.project, name='project'),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name='detail'),
    path('review/', views.review, name='review'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login')
]
