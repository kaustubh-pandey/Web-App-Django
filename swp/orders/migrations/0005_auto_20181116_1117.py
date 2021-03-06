# Generated by Django 2.1.2 on 2018-11-16 05:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20181115_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='delete',
            new_name='isDeleted',
        ),
        migrations.RenameField(
            model_name='manualorder',
            old_name='delete',
            new_name='isDeleted',
        ),
        migrations.RenameField(
            model_name='orderhistory',
            old_name='delete',
            new_name='isDeleted',
        ),
        migrations.RenameField(
            model_name='orderlist',
            old_name='delete',
            new_name='isDeleted',
        ),
        migrations.AlterField(
            model_name='items',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 5, 47, 18, 411670, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='manualorder',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 5, 47, 18, 412366, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 5, 47, 18, 414383, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='orderlist',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 5, 47, 18, 413443, tzinfo=utc)),
        ),
    ]
