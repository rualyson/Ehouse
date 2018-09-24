from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('novo_anuncio', views.novo_anuncio, name='novo_anuncio'),
    path('meus_anuncios', views.meus_anuncios,name='meus_anuncios'),
]