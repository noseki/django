from django.contrib.auth.views import LoginView, LogoutView
from . import forms

class LoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "keijiapp/login.html" 

class LogoutView(LogoutView):
    template_name = "keijiapp/login.html"