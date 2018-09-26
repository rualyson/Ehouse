from django.urls import include, path
from . import views

# We are adding a URL called /home
urlpatterns = [
    path('', views.home, name='home'),
    path('minhaconta/', views.minhaconta, name='minhaconta'),
    path('buscar/', views.buscar, name='buscar'),
]