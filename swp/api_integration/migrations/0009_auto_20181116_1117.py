# Generated by Django 2.1.2 on 2018-11-16 05:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api_integration', '0008_auto_20181115_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='delete',
            new_name='isDeleted',
        ),
        migrations.AlterField(
            model_name='student',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 16, 5, 47, 18, 635665, tzinfo=utc)),
        ),
    ]
