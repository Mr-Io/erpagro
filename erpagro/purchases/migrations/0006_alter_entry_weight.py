# Generated by Django 4.2.2 on 2023-06-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0005_alter_entry_agrofood_alter_entry_entrynote_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='weight',
            field=models.DecimalField(decimal_places=0, max_digits=8, verbose_name='peso neto'),
        ),
    ]
