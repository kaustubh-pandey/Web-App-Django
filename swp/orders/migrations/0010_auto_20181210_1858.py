# Generated by Django 2.1.2 on 2018-12-10 13:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20181210_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 425176, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='manualorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 425176, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 425176, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 13, 28, 20, 425176, tzinfo=utc)),
        ),
    ]
