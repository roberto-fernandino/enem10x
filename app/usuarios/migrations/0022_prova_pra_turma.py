# Generated by Django 4.2.4 on 2023-09-11 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0019_provacriadaprofessor'),
        ('usuarios', '0021_alter_mediageral_media_ciencias_humanas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prova_pra_Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prova', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiais.provacriadaprofessor')),
            ],
        ),
    ]
