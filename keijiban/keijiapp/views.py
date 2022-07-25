from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import ThreadModel
from .forms import SignupForm, LoginForm
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import LoginForm, SignupForm # ユーザーアカウントフォーム
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

class ThreadListView(LoginRequiredMixin, ListView):
    template_name = "keijiapp/list.html"
    model = ThreadModel

    def get_queryset(self):
        return ThreadModel.objects.order_by('-id')

class ThreadCreateView(CreateView):
    template_name = "keijiapp/create.html"
    model = ThreadModel
    fields = ('title','content',)
    readonly_fields = ('created_time', 'updated_time')
    success_url = reverse_lazy('list')

class ThreadDetailView(DetailView):
    template_name = "keijiapp/detail.html"
    model = ThreadModel
    
class ThreadUpdateView(UpdateView):
    template_name = "keijiapp/update.html"
    model = ThreadModel
    fields = ('title','content',)
    readonly_fields = ('created_time', 'updated_time')
    success_url = reverse_lazy('list')

class ThreadDeleteView(DeleteView):
    template_name = "keijiapp/delete.html"
    model = ThreadModel
    success_url = reverse_lazy('list')

class ThreadLoginView(LoginView):
    form_class = LoginForm
    template_name = "keijiapp/login.html" 

class ThreadLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "keijiapp/login.html"

class  ThreadSignupView(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "login_form": LoginForm(),
        "signup_form":SignupForm(),
        }

    
    def get(self,request):
        self.params["login_form"] = LoginForm()
        self.params["signup_form"] = SignupForm()
        self.params["AccountCreate"] = False
        return render(request,"keijiapp/signup.html",context=self.params)

    
    def post(self,request):
        self.params["login_form"] = LoginForm(data=request.POST)
        self.params["signup_form"] = SignupForm(data=request.POST)

        
        # フォーム入力の有効検証
        if self.params["login_form"].is_valid() and self.params["signup_form"].is_valid():

            account = self.params["login_form"].save()
            
            account.set_password(account.password)
            
            account.save()

    
            add_account = self.params["signup_form"].save(commit=False)
            add_account.user = account


            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

        
            add_account.save()

            
            self.params["AccountCreate"] = True

        else:
            
            print(self.params["login_form"].errors)
        
        return render(request,"keijiapp/signup.html",context=self.params)

'''
class ThreadSignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'keijiapp/signup.html'
    success_url = reverse_lazy('list')
'''