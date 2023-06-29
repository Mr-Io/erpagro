# Generated by Django 4.2.2 on 2023-06-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0009_alter_entry_packaging_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='precio por kg'),
        ),
    ]
