# Generated by Django 2.1.2 on 2018-12-09 19:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api_integration', '0011_auto_20181210_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 9, 19, 19, 32, 462102, tzinfo=utc)),
        ),
    ]
