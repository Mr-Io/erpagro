# Generated by Django 4.2.2 on 2023-12-05 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_agent_country'),
        ('packaging', '0008_alter_transaction_transaction_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactiongroup',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='base.agent', verbose_name='agente'),
        ),
        migrations.AddField(
            model_name='transactiongroup',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='fecha'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='packaging.transactiongroup', verbose_name='archivos'),
        ),
    ]
