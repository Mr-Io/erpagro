# Generated by Django 4.2.2 on 2023-07-20 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_company_serial_alter_company_tax_start'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='serial',
        ),
        migrations.AddField(
            model_name='company',
            name='post_box',
            field=models.CharField(default='24', max_length=2, verbose_name='apdo. correos'),
        ),
    ]
