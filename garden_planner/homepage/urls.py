from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),  # Signup form
    path('createaccount/', views.create_account_view, name='createaccount'), 
    path('mainpage/', views.mainpage_view, name='mainpage'),
    path('userdetails/', views.userdetails_view, name='userdetails'),
    path('apple/', views.apple_view, name='apple'),
]