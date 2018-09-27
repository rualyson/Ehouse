from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name ='product_list'),
    path('novo_anuncio', views.product_new, name='new_anuncio'),
    path('meus_anuncio', views.product_new, name='new_anuncio'),
]