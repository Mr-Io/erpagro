# Generated by Django 4.2.2 on 2023-07-26 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0019_invoice_doc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='doc',
            new_name='doc_link',
        ),
    ]
