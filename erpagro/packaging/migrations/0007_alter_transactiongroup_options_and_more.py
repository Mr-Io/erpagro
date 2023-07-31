# Generated by Django 4.2.2 on 2023-12-01 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('packaging', '0006_transactiongroup_remove_transaction_pdf_file_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactiongroup',
            options={'verbose_name': 'archivos pdf'},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='packaging.transactiongroup', verbose_name='archivos'),
        ),
    ]
