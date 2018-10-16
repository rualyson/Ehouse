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
