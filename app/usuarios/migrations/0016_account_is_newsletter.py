# Generated by Django 4.2.4 on 2023-09-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0015_account_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_newsletter',
            field=models.BooleanField(default=True, verbose_name='Newsletter'),
        ),
    ]
