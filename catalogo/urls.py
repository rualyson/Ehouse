from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name ='product_list'),
    path('novo_anuncio', views.product_new, name='novo_anuncio'),
    path('delete_anuncio/<int:id>/', views.product_delete, name="product_delete"),
    path('edit_anuncio/<int:id>/', views.edit_delete, name="update_produto"),
    path('detalhes_anuncio/<int:id>/', views.detalhes_anuncio, name="detalhes_anuncio"),
]