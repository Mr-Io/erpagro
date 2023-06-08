# Generated by Django 4.2.2 on 2023-06-16 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='nombre')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='precio unitario')),
                ('destare_in', models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='destare entrada')),
                ('destare_out', models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='destare salida')),
                ('min_stock', models.PositiveIntegerField(blank=True, null=True, verbose_name='stock mínimo')),
                ('material', models.CharField(choices=[('plastico', 'Plástico'), ('madera', 'Madera'), ('carton', 'Cartón'), ('ifco', 'IFCO')], max_length=32, verbose_name='tipo')),
                ('type', models.CharField(choices=[('caja', 'Caja'), ('pallet', 'Pallet')], max_length=32, verbose_name='tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField(verbose_name='número')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='fecha')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='base.agent', verbose_name='agente')),
                ('packaging', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='packaging.packaging', verbose_name='type')),
            ],
            options={
                'verbose_name': 'movimiento',
            },
        ),
    ]