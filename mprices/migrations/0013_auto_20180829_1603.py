# Generated by Django 2.1 on 2018-08-29 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mprices', '0012_phone_gsm_arena'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='extra',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='extra_display',
        ),
        migrations.AlterField(
            model_name='phone',
            name='sim',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
