from django.views.generic import ListView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ThreadModel
from . import forms
from django.urls import reverse_lazy

class ListView(LoginRequiredMixin, ListView):
    template_name = "keijiapp/list.html"
    model = ThreadModel

class FormView(LoginRequiredMixin, FormView):
    template_name = "keijiapp/form.html"
    model = ThreadModel
    fields = ('title','content', 'created_time', 'updated_time')
    success_url = reverse_lazy('list')

class LoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "keijiapp/login.html" 

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "keijiapp/login.html"