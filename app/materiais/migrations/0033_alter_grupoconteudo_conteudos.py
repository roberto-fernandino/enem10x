# Generated by Django 4.2.4 on 2023-09-25 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0032_remove_conteudo_proporcao_grupoconteudo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupoconteudo',
            name='conteudos',
            field=models.ManyToManyField(to='materiais.conteudo'),
        ),
    ]
