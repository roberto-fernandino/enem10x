# Generated by Django 4.2.4 on 2023-09-06 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0012_alter_simulado_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='questao',
            name='indentificador_unico',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]