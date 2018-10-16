from django.db import models
from django.utils.text import slugify

class Category(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
         return self.name

class Product(models.Model):

    name = models.CharField('Título do anúncio', max_length=100, null=True)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey('catalogo.Category', verbose_name='Categoria', on_delete='models.CASCADE')
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

class Imovel(models.Model):
    categoria = models.ForeignKey(Category, related_name='imoveis', on_delete='models.CASCADE')
    titulo = models.CharField('Título do anúncio', max_length=100, null=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    imagem = models.ImageField('Imagem', upload_to='products', blank=True, null=True)
    descricao = models.TextField(blank=True)
    dono = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    numero = models.CharField(max_length=5)
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200, db_index=True)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    cep = models.CharField(max_length=9)
    disponivel = models.BooleanField(default=True)
    data_cadastramento = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def _get_unique_slug(self):
        slug = slugify(self.titulo)
        unique_slug = slug
        num = 1
        while Imovel.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['cidade']
        verbose_name = 'imovel'
        verbose_name_plural = 'imoveis'
     
    def __str__(self):
        return self.titulo

    