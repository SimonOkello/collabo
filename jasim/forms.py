from django import forms

class LoginForm(forms.Form):
  email = forms.EmailField(label='Email')
  password = forms.CharField(label='Password', max_length=100)

class SignupForm(forms.Form):
  username = forms.CharField(label='Username', max_length=100)
  email = forms.EmailField(label='Email')
  password = forms.CharField(label='Password', max_length=100)

class ProjectForm(forms.Form):
  title = forms.CharField(label='Project Title', max_length=100)
  description = forms.TextField(label='Description')
  created_on = forms.DateField(label='Created on')
  duration = forms.CharField(label='Duration', max_length=100)
  client_website = forms.CharField(label='Clients Website', max_length=100)
  client_name = forms.CharField(label='Client Name', max_length=100)
  client_email = forms.CharField(label='Client Email', max_length=100)
  project_url = forms.CharField(label='Project URL', max_length=100)
