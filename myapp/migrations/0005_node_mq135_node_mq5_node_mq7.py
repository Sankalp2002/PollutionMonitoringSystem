# Generated by Django 4.0.3 on 2022-04-15 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_pollution_data_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='mq135',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='node',
            name='mq5',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='node',
            name='mq7',
            field=models.FloatField(blank=True, default=0),
        ),
    ]