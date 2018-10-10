from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .forms import ImovelForm
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login")
def categorias(request):
       return render(request, 'base.html')

@login_required(login_url="/accounts/login")
def product_list(request):
       context = {
              'imoveis': Imovel.objects.all()}
       return render(request, 'catalogo/product_list.html', context)

@login_required(login_url="/accounts/login")
def product_new(request):
    form = ImovelForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'catalogo/novo_anuncio.html', {'form': form})

@login_required(login_url="/accounts/login")
def product_delete(request, id):
    imovel = Imovel.objects.get(id=id)
    imovel.delete()
    return redirect('product_list')

@login_required(login_url="/accounts/login")
def edit_delete(request, id):
    imovel = Imovel.objects.get(id=id)
    form = ImovelForm(request.POST or None, instance=imovel)
    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'catalogo/update_produto.html', {'form': form})

