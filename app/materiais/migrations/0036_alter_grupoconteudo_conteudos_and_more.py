# Generated by Django 4.2.4 on 2023-10-03 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0035_alter_grupoconteudo_conteudos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupoconteudo',
            name='conteudos',
            field=models.ManyToManyField(blank=True, related_name='grupo', to='materiais.conteudo'),
        ),
        migrations.AlterField(
            model_name='grupoconteudo',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupo', to='materiais.materia'),
        ),
    ]
