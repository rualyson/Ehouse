from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from accounts.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm

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
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, template_name, {'form': form})
