# Generated by Django 4.2.2 on 2023-07-24 18:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quality', '0002_alter_warehouse_agrofoodtypes'),
        ('purchases', '0017_remove_invoice_paid_remove_invoice_settled_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrieragent',
            name='carrier_price',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0001)], verbose_name='precio porte'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='analisis',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0001)], verbose_name='ANÁLISIS'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='comision',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0001)], verbose_name='COMISIÓN'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='descarga',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0001)], verbose_name='DESCARGA'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='embalajes',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0001)], verbose_name='EMBALAJES'),
        ),
        migrations.AlterField(
            model_name='charge',
            name='portes',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0001)], verbose_name='PORTES'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='precio'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quality.warehouse', verbose_name='nave'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='weight',
            field=models.DecimalField(decimal_places=0, max_digits=8, validators=[django.core.validators.MinValueValidator(1)], verbose_name='peso neto'),
        ),
        migrations.AlterField(
            model_name='entrynote',
            name='analisis',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0001)], verbose_name='ANÁLISIS'),
        ),
        migrations.AlterField(
            model_name='entrynote',
            name='carrier_price',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0001)], verbose_name='precio porte'),
        ),
        migrations.AlterField(
            model_name='entrynote',
            name='comision',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0001)], verbose_name='COMISIÓN'),
        ),
        migrations.AlterField(
            model_name='entrynote',
            name='descarga',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0001)], verbose_name='DESCARGA'),
        ),
        migrations.AlterField(
            model_name='entrynote',
            name='embalajes',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0001)], verbose_name='EMBALAJES'),
        ),
        migrations.AlterField(
            model_name='entrynote',
            name='portes',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0.0001)], verbose_name='PORTES'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='settlement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='purchases.settlement', verbose_name='liquidación'),
        ),
    ]
