# Generated by Django 4.2.4 on 2023-08-27 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0007_remove_questao_conteudo_questao_conteudo'),
    ]

    operations = [
        migrations.AddField(
            model_name='provacompleta',
            name='materias',
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='provacompleta',
            name='nota',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='questao',
            name='conteudo',
            field=models.ManyToManyField(blank=True, default=None, related_name='questoes', to='materiais.conteudo'),
        ),
    ]