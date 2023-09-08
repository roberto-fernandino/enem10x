# Generated by Django 4.2.4 on 2023-09-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0013_alter_notas_options_mediageral'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_professor',
            field=models.BooleanField(default=False, verbose_name='Professor'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_aluno',
            field=models.BooleanField(default=False, verbose_name='Aluno'),
        ),
    ]
