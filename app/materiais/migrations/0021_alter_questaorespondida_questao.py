# Generated by Django 4.2.4 on 2023-09-11 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0020_alter_questaorespondida_questao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questaorespondida',
            name='questao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='materiais.questao'),
        ),
    ]
