from django.db import models
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    nome = models.CharField('Nome Completo', max_length = 150)
    idade = models.IntegerField('Idade:')
    cpf = models.IntegerField('CPF:')    
    cidade = models.CharField('Cidade:', max_length=150, blank=True)
    cep = models.CharField('CEP:', max_length=8, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.nome

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()