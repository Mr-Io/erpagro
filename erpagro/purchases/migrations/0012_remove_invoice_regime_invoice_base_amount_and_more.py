# Generated by Django 4.2.2 on 2023-07-18 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0011_invoice_irpf_invoice_vat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='regime',
        ),
        migrations.AddField(
            model_name='invoice',
            name='base_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='total'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='expenses_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='gastos'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='irpf_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='retención'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='tax_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='base imponible'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='total'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='type',
            field=models.CharField(blank=True, choices=[('G', 'Reg. General'), ('E', 'Reg. Esp. Agrario')], max_length=1, verbose_name='tipo'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='vat_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='IVA'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='irpf',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='%IRPF'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='vat',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='%IVA'),
        ),
    ]
