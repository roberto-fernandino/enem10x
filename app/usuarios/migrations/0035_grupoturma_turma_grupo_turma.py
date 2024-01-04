# Generated by Django 4.2.4 on 2023-12-28 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0034_escola_cordernador'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoTurma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='turma',
            name='grupo_turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.grupoturma'),
        ),
    ]