# Generated by Django 4.2.4 on 2023-09-11 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0021_alter_questaorespondida_questao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submateria',
            name='materia',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_materia', to='materiais.materia'),
        ),
    ]