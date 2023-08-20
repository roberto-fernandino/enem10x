# Generated by Django 4.2.4 on 2023-08-20 18:27

from django.db import migrations, models
import django.db.models.deletion
import materiais.funcs


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=10)),
                ('peso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubMateria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Questoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chave', models.CharField(max_length=50)),
                ('enunciado', models.TextField(default=None, null=True)),
                ('imagem', models.ImageField(upload_to=materiais.funcs.define_image_path)),
                ('opcoes', models.JSONField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='materiais.materia')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='materiais.nivel')),
            ],
        ),
        migrations.AddField(
            model_name='materia',
            name='submateria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='materiais.submateria'),
        ),
    ]
