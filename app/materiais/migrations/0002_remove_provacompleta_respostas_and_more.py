# Generated by Django 4.2.4 on 2023-08-23 01:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materiais', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provacompleta',
            name='respostas',
        ),
        migrations.AddField(
            model_name='provarespondida',
            name='prova_completa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='materiais.provacompleta'),
        ),
        migrations.AddField(
            model_name='provarespondida',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='conteudo',
            name='sub_materia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materiais.submateria'),
        ),
        migrations.AlterField(
            model_name='provacompleta',
            name='nota',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='provarespondida',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiais.questao'),
        ),
        migrations.CreateModel(
            name='QuestaoRespondida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='materiais.questao')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
