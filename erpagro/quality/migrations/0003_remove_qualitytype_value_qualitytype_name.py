# Generated by Django 4.2.2 on 2023-06-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0002_rename_agrofood_types_warehouse_agrofoodtypes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualitytype',
            name='value',
        ),
        migrations.AddField(
            model_name='qualitytype',
            name='name',
            field=models.CharField(max_length=256, null=True, verbose_name='nombre'),
        ),
    ]
