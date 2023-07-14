# Generated by Django 4.2.2 on 2023-07-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0021_invoice_pdf_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='pdf_file',
        ),
        migrations.AddField(
            model_name='settlement',
            name='pdf_file',
            field=models.FileField(blank=True, upload_to='purchases/settlement'),
        ),
    ]
