# Generated by Django 4.0.3 on 2022-05-06 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_node_macaddress_alter_node_installeddate'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollution_data',
            name='macAddress',
            field=models.CharField(default='None', max_length=128),
        ),
    ]
