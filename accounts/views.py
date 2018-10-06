from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from accounts.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CadastroCliente
from .models import Cliente

#Create your views here
def cadastro(request):
    template_name = 'usuarios/cadastro.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('cadastro_cliente')
    else:
        form = RegisterForm()
    return render(request, template_name, {'form': form})

def cadastro_cliente(request):
    template_name = 'usuarios/cadastro_cliente.html'
    form = CadastroCliente(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request, template_name, {'form': form})

def meucadastro(request):
    context = {
              'clientes': Cliente.objects.all() }
    return render(request,'usuarios/meucadastro.html', context)

def editarcadastro(request, id):
    cliente = Cliente.objects.get(id=id)
    form = CadastroCliente(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('/meucadastro/')    
    redirect (request, '/usuarios/editarcadastro.html', {'form':form})

