# Generated by Django 4.2.2 on 2023-07-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0025_entrynote_pdf_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='serial',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='serial',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='serie'),
        ),
    ]