# Generated by Django 4.2.2 on 2023-07-26 19:17

import archive.pdfutils.filepath
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0024_remove_invoice_doc_link_invoice_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrynote',
            name='pdf_file',
            field=models.FileField(blank=True, max_length=256, upload_to=archive.pdfutils.filepath.get_filepath, verbose_name='archivo'),
        ),
    ]
