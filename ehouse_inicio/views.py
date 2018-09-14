from ehouse_inicio.models import UsuarioForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required(login_url="login/")

def home(request):
	return render(request,"home.html")

@login_required   
def anuncios(request):
	return render(request,"anuncios.html")

