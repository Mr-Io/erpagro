# Generated by Django 4.2.2 on 2023-06-16 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgrofoodFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'familia género',
                'verbose_name_plural': 'familias género',
            },
        ),
        migrations.CreateModel(
            name='AgrofoodSubfamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='nombre')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subfamilies', to='product.agrofoodfamily', verbose_name='familia')),
            ],
            options={
                'verbose_name': 'subfamilia género',
                'verbose_name_plural': 'subfamilias género',
            },
        ),
        migrations.CreateModel(
            name='AgrofoodType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='nombre')),
                ('price_min', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='precio mín. coste')),
                ('quality', models.CharField(choices=[('I', 'Primera'), ('II', 'Segunda'), ('AVENADO', 'Avenado')], max_length=8, verbose_name='calidad')),
                ('subfamily', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='product.agrofoodsubfamily', verbose_name='subfamilia')),
            ],
            options={
                'verbose_name': 'tipo de género',
                'verbose_name_plural': 'tipos de género',
            },
        ),
    ]
