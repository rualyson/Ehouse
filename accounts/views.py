from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from accounts.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import ProfileForm
from .models import Profile
from django.db import transaction


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
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, template_name, {'form': form})


def cadastro_cliente(request):
    template_name = 'usuarios/cadastro_cliente.html'
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')
    else:
        form = ProfileForm()
    return render(request, template_name, {'form': form})

@login_required
@transaction.atomic
def meucadastro(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Seu perfil foi atualizado!'))
            return redirect('home')
        else:
            messages.error(request, ('Por favor, preencha os dados corretamente!'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'usuarios/meucadastro.html', {
        'profile_form': profile_form
    })
    

@login_required
@transaction.atomic
def editarcadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Seu perfil foi atualizado!'))
            return redirect('home')
        else:
            messages.error(request, ('Por favor, preencha os dados corretamente!'))
    else:
        form = UserCreationForm(instance=request.user)
    return render(request, 'usuarios/editarcadastro.html', {
        'form': form
    })