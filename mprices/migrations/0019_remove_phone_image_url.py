# Generated by Django 2.1 on 2018-09-10 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mprices', '0018_auto_20180910_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='image_url',
        ),
    ]
