# Generated by Django 4.2.2 on 2023-08-01 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packaging', '0001_initial'),
        ('purchases', '0027_alter_invoice_serial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='packaging_transaction',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='packaging.transaction', verbose_name='Envases'),
        ),
    ]
