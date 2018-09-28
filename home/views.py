from accounts.forms import LoginForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def home(request):
	return render(request,"inicio.html")

@login_required(login_url="/accounts/login")
def minhaconta(request):
	return render(request,"minhaconta.html")

@login_required(login_url="/accounts/login")
def buscar(request):
	return render(request,"buscar.html")
