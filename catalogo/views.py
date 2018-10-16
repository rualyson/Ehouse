from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from .forms import ImovelForm
from django.contrib.auth.decorators import login_required
from django.views import generic

from watson import search as watson
from django.db import models


class ImovelListView(generic.ListView):

    queryset = Imovel.objects.all()

    template_name = 'catalogo/product_list.html'
    context_object_name = 'imoveis'
    paginate_by = 1

    def get_queryset(self):
        queryset = Imovel.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)
        return queryset



product_list = ImovelListView.as_view()


class CategoryListView(generic.ListView):

    template_name = 'catalogo/category.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Imovel.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


category = CategoryListView.as_view()


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

@login_required(login_url="/accounts/login")
def detalhes_anuncio(request, id):
    
    imovel = Imovel.objects.get(id=id)
    form = ImovelForm(request.POST or None, instance=imovel)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'catalogo/detalhes_anuncio.html', {'form': form})

def buscarCep(request):
    buscar = request.POST['cep']
    imovel = Imovel.objects.filter(cep__contains= 'buscar')
    return render(request, 'catalogo/busca.html', {'imovel':imovel})
