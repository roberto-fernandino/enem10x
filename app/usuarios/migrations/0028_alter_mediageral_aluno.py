# Generated by Django 4.2.4 on 2023-09-17 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0027_remove_mediageral_usuario_mediageral_aluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediageral',
            name='aluno',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.aluno'),
        ),
    ]