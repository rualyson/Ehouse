from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from django.contrib.auth import login, authenticate
from accounts.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import ProfileForm
from .models import Profile

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
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request, template_name, {'form': form})

def meucadastro(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        user = request.user
        profile = user.profile
        form = ProfileForm(instance = profile)
    args = {}
    # args.update(csrf(request))

    args['form'] = form
    return render_to_response('usuarios/meucadastro.html', args)

def editarcadastro(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/meucadastro/')
    else:
        user = request.user
        profile = user.profile
        form = ProfileForm(instance = profile)
    args = {}
    # args.update(csrf(request))

    args['form'] = form
    return render_to_response('usuarios/meucadastro.html', args)
