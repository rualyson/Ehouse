# Generated by Django 2.1.1 on 2018-10-09 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20181009_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tipo',
            field=models.ForeignKey(default='', null=True, on_delete='models.CASCADE', to='catalogo.Tipo', verbose_name='Tipo'),
        ),
    ]
