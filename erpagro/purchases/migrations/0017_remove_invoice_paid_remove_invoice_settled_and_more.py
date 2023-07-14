# Generated by Django 4.2.2 on 2023-07-21 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0016_alter_charge_comision_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='settled',
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='fecha')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='purchases.supplier')),
            ],
            options={
                'verbose_name': 'liquidación',
                'verbose_name_plural': 'liquidaciones',
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='settlement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='purchases.settlement', verbose_name='liquidación'),
        ),
    ]
