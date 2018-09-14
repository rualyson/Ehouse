#!python
from django.urls import include, path
from . import views

# We are adding a URL called /home
urlpatterns = [
    path('', views.home, name='home'),
    path('anuncios', views.anuncios, name='anuncios'),
]
