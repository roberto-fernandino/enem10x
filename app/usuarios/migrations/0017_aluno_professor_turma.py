# Generated by Django 4.2.4 on 2023-09-03 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0016_account_is_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alunos', models.IntegerField()),
                ('total_alunos', models.IntegerField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Professores',
            },
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=180, unique=True)),
                ('data_criada', models.DateTimeField(auto_now_add=True)),
                ('alunos', models.ManyToManyField(to='usuarios.aluno')),
                ('criador', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='criador_turma', to='usuarios.professor')),
                ('professores', models.ManyToManyField(to='usuarios.professor')),
            ],
        ),
    ]
