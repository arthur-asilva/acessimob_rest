# Generated by Django 4.1.1 on 2022-10-09 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_location', '0002_rename_created_at_postlocation_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlocation',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
