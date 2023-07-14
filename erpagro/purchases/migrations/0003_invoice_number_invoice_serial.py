# Generated by Django 4.2.2 on 2023-07-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='number',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='número'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='serial',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='serie'),
        ),
    ]
