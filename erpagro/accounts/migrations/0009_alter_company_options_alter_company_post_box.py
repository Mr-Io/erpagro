# Generated by Django 4.2.2 on 2023-07-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_company_address_line2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Empresa', 'verbose_name_plural': 'Datos Empresa'},
        ),
        migrations.AlterField(
            model_name='company',
            name='post_box',
            field=models.CharField(blank=True, max_length=2, verbose_name='apdo. correos'),
        ),
    ]
