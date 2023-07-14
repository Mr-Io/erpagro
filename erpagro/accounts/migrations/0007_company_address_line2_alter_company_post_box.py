# Generated by Django 4.2.2 on 2023-07-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_company_serial_company_post_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address_line2',
            field=models.CharField(blank=True, max_length=46, verbose_name='dirección 2'),
        ),
        migrations.AlterField(
            model_name='company',
            name='post_box',
            field=models.CharField(max_length=2, verbose_name='apdo. correos'),
        ),
    ]
