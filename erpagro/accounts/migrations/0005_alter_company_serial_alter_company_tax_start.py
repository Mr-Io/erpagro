# Generated by Django 4.2.2 on 2023-07-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_company_serial_company_tax_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='serial',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='company',
            name='tax_start',
            field=models.DateField(verbose_name='inicio fiscal'),
        ),
    ]
