from django.shortcuts import render
from .forms import *
from .models import *
from .forms import ProductForm

def categorias(request):
       return render(request, 'base.html')


def product_list(request):
       context = {
              'products': Product.objects.all()}
       return render(request, 'catalogo/product_list.html', context)





def product_new(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'catalogo/novo_anuncio.html', {'form': form})