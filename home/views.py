from accounts.forms import LoginForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required(login_url="/accounts/login")

def home(request):
	return render(request,"home.html")
