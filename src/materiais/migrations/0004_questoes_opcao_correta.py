# Generated by Django 4.2.4 on 2023-08-20 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0003_alter_nivel_options_alter_questoes_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questoes',
            name='opcao_correta',
            field=models.CharField(default=None, max_length=1, null=True),
        ),
    ]