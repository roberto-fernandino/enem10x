# Generated by Django 4.2.4 on 2023-08-31 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_alter_account_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediageral',
            name='media_ciencias_humanas',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='mediageral',
            name='media_ciencias_natureza',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='mediageral',
            name='media_linguagens',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='mediageral',
            name='media_matematica',
            field=models.FloatField(default=0, null=True),
        ),
    ]
