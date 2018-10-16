from .models import Category, Product, Imovel


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def product(request):
    return {
        'product': Product.objects.all()
    }
def imoveis(request):
    return {
        'imoveis': Imovel.objects.all()
    }