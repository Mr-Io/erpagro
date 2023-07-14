# Generated by Django 4.2.2 on 2023-07-18 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_alter_regime_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regime',
            name='type',
            field=models.CharField(choices=[('G', 'Reg. General'), ('E', 'Reg. Esp. Agrario')], max_length=1, verbose_name='tipo'),
        ),
    ]
