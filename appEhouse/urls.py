from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from aluguel.forms import LoginForm, UserModelForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aluguel.urls')),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html', authentication_form = LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = '/login')), 
 
]
