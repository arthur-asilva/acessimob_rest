# Generated by Django 4.1.1 on 2022-10-09 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_location', '0004_alter_postlocation_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postlocation',
            name='created_date',
        ),
        migrations.AddField(
            model_name='postlocation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 9, 18, 1, 19, 270639), null=True),
        ),
    ]