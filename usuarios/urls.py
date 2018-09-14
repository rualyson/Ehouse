from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from ehouse_inicio.models import Usuario, UsuarioForm
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ehouse_inicio.urls')),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name = 'usuarios/login.html', authentication_form = Usuario), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = '/login')), 
 
]
