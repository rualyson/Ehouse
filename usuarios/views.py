from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from usuarios.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm

#Create your views here
def cadastro(request):

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)

            login(request, user)

            return redirect('/')
    else:

        form = SignUpForm()

    args = {
    	'form': form,
    }

    return render(request, 'core/cadastro.html', args)