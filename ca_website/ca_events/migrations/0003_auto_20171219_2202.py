# Generated by Django 2.0 on 2017-12-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_events', '0002_auto_20171219_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicemeeting',
            name='meeting_name',
            field=models.CharField(max_length=100),
        ),
    ]