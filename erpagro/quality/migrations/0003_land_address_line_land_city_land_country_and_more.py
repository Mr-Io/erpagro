# Generated by Django 4.2.2 on 2023-07-31 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0002_alter_warehouse_agrofoodtypes'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='address_line',
            field=models.CharField(blank=True, max_length=46, verbose_name='dirección'),
        ),
        migrations.AddField(
            model_name='land',
            name='city',
            field=models.CharField(blank=True, max_length=30, verbose_name='población'),
        ),
        migrations.AddField(
            model_name='land',
            name='country',
            field=models.CharField(blank=True, choices=[('ES', 'ESPAÑA'), ('PT', 'PORTUGAL'), ('IT', 'ITALIA')], max_length=2, verbose_name='país'),
        ),
        migrations.AddField(
            model_name='land',
            name='postal_code',
            field=models.CharField(blank=True, max_length=5, verbose_name='código postal'),
        ),
        migrations.AddField(
            model_name='land',
            name='state',
            field=models.CharField(blank=True, max_length=30, verbose_name='provincia'),
        ),
    ]
