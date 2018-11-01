# Generated by Django 2.1.1 on 2018-10-31 23:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogo', '0014_auto_20181030_0416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=1000)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('imovel', models.ForeignKey(on_delete=True, to='catalogo.Imovel')),
                ('user', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]