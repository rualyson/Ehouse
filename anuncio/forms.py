from .models import Anuncio
from django import forms
from django.forms import ModelForm

class AnuncioForm(ModelForm):
    class Meta:
        model = Anuncio
        fields = ['valor', 'cidade', 'cep', 'descricao', 'telefone','foto']