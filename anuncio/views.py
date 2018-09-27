from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Anuncio
from .forms import AnuncioForm
from django.forms import ModelForm

# Create your views here.
@login_required
def meus_anuncios(request):
    anuncios = Anuncio.objects.all()
    return render(request,'meus_anuncios.html', {'anuncios':anuncios})

@login_required
def novo_anuncio(request):
    form = AnuncioForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('meus_anuncios')

    return render(request, 'novo_anuncio.html', {'form': form})
