from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('project/', views.project, name='project'),
    path('detail/', views.detail, name='detail'),
    path('review/', views.review, name='review'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login')
]
