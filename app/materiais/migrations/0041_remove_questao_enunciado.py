# Generated by Django 4.2.4 on 2023-12-12 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0040_alter_grupoconteudo_conteudos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questao',
            name='enunciado',
        ),
    ]
