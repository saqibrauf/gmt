# Generated by Django 2.1 on 2018-08-29 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mprices', '0015_auto_20180829_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='phone_video',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='status',
        ),
        migrations.AlterField(
            model_name='phone',
            name='release',
            field=models.DateTimeField(default=datetime.datetime.today, editable=False),
        ),
    ]
