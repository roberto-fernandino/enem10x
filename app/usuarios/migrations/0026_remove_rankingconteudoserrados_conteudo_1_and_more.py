# Generated by Django 4.2.4 on 2023-09-17 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0029_delete_tipo_provacompleta_simulado'),
        ('usuarios', '0025_provaturma_rankingconteudoserrados_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rankingconteudoserrados',
            name='conteudo_1',
        ),
        migrations.RemoveField(
            model_name='rankingconteudoserrados',
            name='conteudo_2',
        ),
        migrations.RemoveField(
            model_name='rankingconteudoserrados',
            name='conteudo_3',
        ),
        migrations.RemoveField(
            model_name='rankingconteudoserrados',
            name='conteudo_4',
        ),
        migrations.RemoveField(
            model_name='rankingconteudoserrados',
            name='conteudo_5',
        ),
        migrations.RemoveField(
            model_name='rankingconteudoserrados',
            name='materia',
        ),
        migrations.AddField(
            model_name='rankingconteudoserrados',
            name='conteudos',
            field=models.ManyToManyField(to='materiais.conteudo'),
        ),
        migrations.AddField(
            model_name='rankingconteudoserrados',
            name='tipo_simulado',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='materiais.simulado'),
        ),
    ]