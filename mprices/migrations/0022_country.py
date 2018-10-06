# Generated by Django 2.1 on 2018-10-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mprices', '0021_auto_20180928_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=75, unique=True)),
                ('country_slug', models.CharField(blank=True, editable=False, max_length=75)),
            ],
            options={
                'ordering': ['country'],
            },
        ),
    ]
