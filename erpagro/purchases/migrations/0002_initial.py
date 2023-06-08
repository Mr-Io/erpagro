# Generated by Django 4.2.2 on 2023-06-16 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('quality', '0001_initial'),
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='entries', to='quality.warehouse', verbose_name='nave'),
        ),
    ]