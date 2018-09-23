from usuarios.forms import LoginForm
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    # auth
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', auth_views.LogoutView.as_view(next_page = '/login')), 
    path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html', authentication_form = LoginForm), name='login'),
]
