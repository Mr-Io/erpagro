# Generated by Django 4.2.2 on 2023-07-19 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exit',
            name='in_warehouse',
        ),
        migrations.AddField(
            model_name='exit',
            name='sent',
            field=models.BooleanField(default=False, verbose_name='Enviado'),
        ),
    ]
