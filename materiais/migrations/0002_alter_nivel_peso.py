# Generated by Django 4.2.4 on 2023-08-20 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nivel',
            name='peso',
            field=models.FloatField(),
        ),
    ]
