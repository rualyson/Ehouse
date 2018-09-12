from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from aluguel.forms import LoginForm, UserModelForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('aluguel.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),
    
]
