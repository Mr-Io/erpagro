# Generated by Django 4.2.2 on 2023-07-26 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0018_alter_carrieragent_carrier_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='doc',
            field=models.URLField(blank=True, verbose_name='pdf'),
        ),
    ]