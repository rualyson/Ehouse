from accounts.forms import LoginForm
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from . import views

urlpatterns = [

    # auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', auth_views.LogoutView.as_view(next_page = '/')), 
    path('login/', auth_views.LoginView.as_view(template_name = 'usuarios/login.html', authentication_form = LoginForm), name='login'),
   
]