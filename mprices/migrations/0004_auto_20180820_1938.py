# Generated by Django 2.1 on 2018-08-20 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mprices', '0003_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phone',
            old_name='brand_id',
            new_name='brand_name',
        ),
    ]
