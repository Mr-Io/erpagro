# Generated by Django 4.2.2 on 2023-06-29 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packaging', '0002_alter_packaging_type'),
        ('purchases', '0009_alter_entry_packaging_transaction'),
        ('sales', '0003_alter_exit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exit',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='purchases.entry', verbose_name='entrada'),
        ),
        migrations.AlterField(
            model_name='exit',
            name='packaging_transaction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='packaging.transaction'),
        ),
    ]
