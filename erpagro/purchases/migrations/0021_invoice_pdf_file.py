# Generated by Django 4.2.2 on 2023-07-26 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0020_rename_doc_invoice_doc_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='pdf_file',
            field=models.FileField(blank=True, upload_to='puchases_invoices'),
        ),
    ]
