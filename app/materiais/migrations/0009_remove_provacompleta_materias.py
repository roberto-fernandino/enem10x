# Generated by Django 4.2.4 on 2023-08-27 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0008_provacompleta_materias_alter_provacompleta_nota_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provacompleta',
            name='materias',
        ),
    ]
