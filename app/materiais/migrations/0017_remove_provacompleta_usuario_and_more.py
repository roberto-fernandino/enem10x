# Generated by Django 4.2.4 on 2023-09-08 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0021_alter_mediageral_media_ciencias_humanas_and_more'),
        ('materiais', '0016_alter_opcaoimagem_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provacompleta',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='provarespondida',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='questaorespondida',
            name='usuario',
        ),
        migrations.AddField(
            model_name='provacompleta',
            name='aluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.aluno'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='provarespondida',
            name='aluno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.aluno'),
        ),
        migrations.AddField(
            model_name='questaorespondida',
            name='aluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.aluno'),
            preserve_default=False,
        ),
    ]
