# Generated by Django 2.0 on 2017-12-21 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ca_events', '0005_auto_20171221_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
