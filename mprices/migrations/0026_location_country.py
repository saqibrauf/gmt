# Generated by Django 2.1 on 2018-10-05 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mprices', '0025_auto_20181005_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mprices.Country'),
        ),
    ]
