from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login")
def categorias(request):
       return render(request, 'base.html')

@login_required(login_url="/accounts/login")
def product_list(request):
       context = {
              'products': Product.objects.all()}
       return render(request, 'catalogo/product_list.html', context)

@login_required(login_url="/accounts/login")
def product_new(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'catalogo/novo_anuncio.html', {'form': form})

@login_required(login_url="/accounts/login")
def product_delete(request, id):
    produto = Product.objects.get(id=id)
    produto.delete()
    return redirect('product_list')
@login_required(login_url="/accounts/login")
def edit_delete(request, id):
    produto = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'catalogo/update_produto.html', {'form': form}) 

