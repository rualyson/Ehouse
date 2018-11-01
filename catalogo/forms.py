from .models import Product
from .models import Imovel

from django import forms

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'slug', 'price', 'category', 'description')


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = (
            'categoria','id', 'titulo',
            'cidade', 'estado','rua', 'numero', 'bairro', 'cep',
            'imagem','preco',
            'disponivel',
            'descricao'
        )

class Form_Comentario(forms.Form):
    comentario = forms.CharField(max_length=1000, widget=forms.Textarea())