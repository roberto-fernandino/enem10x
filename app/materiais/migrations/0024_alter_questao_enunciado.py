# Generated by Django 4.2.4 on 2023-09-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0023_alter_conteudo_sub_materia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='enunciado',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]