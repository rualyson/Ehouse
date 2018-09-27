from django.contrib import admin
from django.urls import path, include
from catalogo import views as views_catalogo

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('meus_anuncios/', include('anuncio.urls')),
    path('novo_anuncio/', include('anuncio.urls')),
    path('meus_anuncios/', include('anuncio.urls')),
    path('produtos/', include('catalogo.urls')),


]
