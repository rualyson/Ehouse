#!python
#log/views.py
from aluguel.forms import UserModelForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating

@login_required(login_url="login/")


def home(request):
	return render(request,"home.html")

def cadastro(request):
    form = UserModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    return render(request,'cadastro.html',{'form':form})
