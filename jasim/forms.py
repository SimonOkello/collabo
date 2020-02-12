from django import forms

class LoginForm(forms.Form):
  email = forms.EmailField(label='Email')
  password = forms.CharField(label='Password')

class SignupForm(forms.Form):
  username = forms.CharField(label='Username')
  email = forms.EmailField(label='Email')
  password = forms.CharField(label='Password')
