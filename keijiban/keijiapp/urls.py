from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ThreadListView.as_view(), name='list'),
    path('create/', views.ThreadCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.ThreadDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.ThreadUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ThreadDeleteView.as_view(), name='delete'),
    path('', views.ThreadLoginView.as_view(), name='login'),
    path('logout/', views.ThreadLogoutView.as_view(), name= 'logout'),
    path('signup/', views.ThreadSignupView.as_view(), name='signup'),
]