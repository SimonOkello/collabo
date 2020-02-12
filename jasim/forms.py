from django import forms, ModelForm
from . models import User, Project

class LoginForm(forms.ModelForm):
  class Meta:
    model = 'User'
    fields = ('email', 'password')

class SignupForm(forms.ModelForm):
  class Meta:
    model = 'User'
    fields = ('__all__')

class ProjectForm(forms.ModelForm):
  class Meta:
    model = 'Project'
    fields = ('title', 'description', 'created_on', 'duration', 'client_website', 'client_name', 'client_email', 'project_url')
