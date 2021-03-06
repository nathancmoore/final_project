# Generated by Django 2.0 on 2017-12-22 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('event_name', models.CharField(max_length=50)),
                ('start_time', models.CharField(max_length=15)),
                ('location_name', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=250)),
                ('suite', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(max_length=150)),
                ('zip_code', models.IntegerField(null=True)),
                ('room', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('accessibility', models.BooleanField(default=False)),
                ('last_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('event_date', models.DateTimeField(null=True)),
                ('published', models.BooleanField(default=False)),
                ('contact_phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InternalResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, default='', max_length=500)),
                ('upload', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.IntegerField()),
                ('meeting_name', models.CharField(max_length=50)),
                ('weekday', models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], max_length=10)),
                ('start_time', models.CharField(max_length=15)),
                ('end_time', models.CharField(max_length=15)),
                ('location_name', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=250)),
                ('suite', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(max_length=150)),
                ('zip_code', models.IntegerField()),
                ('room', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField()),
                ('duration', models.CharField(max_length=200)),
                ('meeting_format', models.CharField(max_length=30)),
                ('accessibility', models.CharField(max_length=150)),
                ('last_updated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_name', models.CharField(max_length=100)),
                ('meeting_day', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=15)),
                ('location_name', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=250)),
                ('suite', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(max_length=150)),
                ('zip_code', models.IntegerField()),
                ('room', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField()),
                ('last_updated', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
