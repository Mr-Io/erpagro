# Generated by Django 4.2.2 on 2023-07-20 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_agent_mobile_alter_agent_name_and_more'),
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('agent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='base.agent')),
                ('id_unique', models.CharField(default='setting', max_length=7, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Compañía',
            },
            bases=('base.agent',),
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'usuario'},
        ),
    ]