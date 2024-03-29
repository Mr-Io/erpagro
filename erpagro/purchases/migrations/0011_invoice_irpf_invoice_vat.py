# Generated by Django 4.2.2 on 2023-07-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0010_invoice_regime'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='irpf',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='%IRPF'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='vat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='%IVA'),
        ),
    ]
