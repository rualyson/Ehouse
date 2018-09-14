from ehouse_inicio.models import UsuarioForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def cadastro(request):
    form = UsuarioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
    return render(request,'usuarios/cadastro.html',{'form':form})
