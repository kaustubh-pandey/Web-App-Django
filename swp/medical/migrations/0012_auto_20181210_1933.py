# Generated by Django 2.1.2 on 2018-12-10 14:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0011_auto_20181210_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 14, 3, 4, 781389, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicalappointment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 14, 3, 4, 781389, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicalleave',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 10, 14, 3, 4, 781389, tzinfo=utc)),
        ),
    ]
