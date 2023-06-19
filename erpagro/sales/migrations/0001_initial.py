# Generated by Django 4.2.2 on 2023-06-22 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('packaging', '0001_initial'),
        ('base', '0001_initial'),
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('agent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.agent')),
                ('commission', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='COMISIÓN')),
                ('rapell', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='RAPELL')),
                ('porte', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='PORTE')),
                ('fianza', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='FIANZA')),
                ('charge', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Tarifa de gastos')),
            ],
            options={
                'verbose_name': 'cliente',
            },
            bases=('base.agent', models.Model),
        ),
        migrations.CreateModel(
            name='CommissionAgent',
            fields=[
                ('agent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.agent')),
                ('commission', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='COMISIÓN')),
            ],
            options={
                'verbose_name': 'comisionista',
            },
            bases=('base.agent', models.Model),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='COMISIÓN')),
                ('rapell', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='RAPELL')),
                ('porte', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='PORTE')),
                ('fianza', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='FIANZA')),
                ('charge', models.DecimalField(blank=True, decimal_places=4, max_digits=6, null=True, verbose_name='Tarifa de gastos')),
                ('settled', models.BooleanField(default=False, verbose_name='liquidada')),
                ('paid', models.BooleanField(default=False, verbose_name='pagada')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='fecha')),
                ('commission_agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sales.commissionagent', verbose_name='comisionista')),
            ],
            options={
                'verbose_name': 'factura',
            },
        ),
        migrations.CreateModel(
            name='Exit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=1, max_digits=9, verbose_name='peso neto')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='precio por kg')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='fecha')),
                ('in_warehouse', models.BooleanField(default=True, verbose_name='en almacén')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales', to='sales.client', verbose_name='cliente')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sales', to='purchases.entry', verbose_name='entrada')),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sales', to='sales.invoice', verbose_name='factura')),
                ('packaging_transaction', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='packaging.transaction')),
            ],
            options={
                'verbose_name': 'salida',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='commission_agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sales.commissionagent', verbose_name='comisionista'),
        ),
    ]
