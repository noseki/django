from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ListView.as_view(), name='list'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name= 'logout'),
]