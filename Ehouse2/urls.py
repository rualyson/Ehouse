
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('inicio.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
]