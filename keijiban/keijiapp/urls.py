from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ListView.as_view(), name='list'),
    path('form/', views.FormView.as_view(), name="form"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name= 'logout'),
]