from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome Completo', max_length = 150)
    idade = models.IntegerField('Ex: 30')
    cpf = models.IntegerField('000.000.000-00')
    cep = models.CharField('00000-000', max_length=8)
    cidade = models.CharField('Ex: Rio de Janeiro', max_length=150)

    def __str__(self):
        return self.nome + ' ' + self.cidade
    