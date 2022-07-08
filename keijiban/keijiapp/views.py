from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import ThreadModel
from .forms import SignupForm, LoginForm
from django.urls import reverse_lazy

class ListView(LoginRequiredMixin, ListView):
    template_name = "keijiapp/list.html"
    model = ThreadModel

    def get_queryset(self):
        return ThreadModel.objects.order_by('-id')

class CreateView(CreateView):
    template_name = "keijiapp/create.html"
    model = ThreadModel
    fields = ('title','content')
    success_url = reverse_lazy('list')

class DetailView(DetailView):
    template_name = "keijiapp/detail.html"
    model = ThreadModel
    
class UpdateView(UpdateView):
    template_name = "keijiapp/update.html"
    model = ThreadModel
    fields = ('title','content')
    success_url = reverse_lazy('list')

class DeleteView(DeleteView):
    template_name = "keijiapp/delete.html"
    model = ThreadModel
    success_url = reverse_lazy('list')

class LoginView(LoginView):
    form_class = LoginForm
    template_name = "keijiapp/login.html" 

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "keijiapp/login.html"

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'keijiapp/signup.html'
    success_url = reverse_lazy('list')