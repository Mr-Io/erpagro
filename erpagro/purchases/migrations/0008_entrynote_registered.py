# Generated by Django 4.2.2 on 2023-06-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0007_alter_entry_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrynote',
            name='registered',
            field=models.BooleanField(default=False, verbose_name='registrado'),
        ),
    ]