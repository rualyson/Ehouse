from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField('Nome Completo', max_length = 150)
    idade = models.IntegerField('Idade:')
    cpf = models.IntegerField('CPF:')
    cep = models.CharField('CEP:', max_length=8)
    cidade = models.CharField('Cidade:', max_length=150)
    bio = models.TextField(blank=True)

    User.profile = property(lambda u: Profile.objects.get_or_create(user = u)[0])

    def __str__(self):
        return self.nome


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.created(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()