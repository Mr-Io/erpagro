# Generated by Django 4.2.2 on 2023-06-25 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='carrier_price',
        ),
    ]
