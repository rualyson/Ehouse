from django.contrib import admin

# Register your models here.

from .models import Product, Category, Imovel


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']
    actions = []

class ImovelAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'data_cadastramento', 'data_atualizacao']
    search_fields = ['name', 'slug']
    list_filter = ['data_cadastramento', 'data_atualizacao']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Imovel,ImovelAdmin)