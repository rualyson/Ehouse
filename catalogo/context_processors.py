from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def product(request):
    return {
        'product': Product.objects.all()
    }
