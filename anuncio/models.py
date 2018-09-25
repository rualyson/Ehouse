from django.db import models
from django.forms import ModelForm

# Create your models here.
class Anuncio(models.Model):
    valor = models.DecimalField (max_digits=5, decimal_places=2)
    cidade = models.CharField (max_length = 200)
    cep = models.CharField (max_length = 200)
    descricao = models.TextField ()
    telefone = models.CharField (max_length = 200)
    foto = models.ImageField (upload_to='fotos_anuncios')

    def __str__(self):
        return self.valor, self.cidade, self.cep, self.descricao, self.contato,
        self.foto
 