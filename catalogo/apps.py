
from django.apps import AppConfig

from watson import search as watson


class CatalogoConfig(AppConfig):
    name = 'catalogo'
    verbose_name = 'Catálogo'

    def ready(self):
        Imovel = self.get_model('Imovel')
        watson.register(Imovel)