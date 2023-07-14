# Generated by Django 4.2.2 on 2023-07-19 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0014_alter_invoice_options_entrynote_analisis_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='comision',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='COMISIÓN [%]'),
        ),
        migrations.AlterField(
            model_name='entrynote',
            name='comision',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='COMISIÓN [%]'),
        ),
    ]
