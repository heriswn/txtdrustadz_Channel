# Generated by Django 3.2.4 on 2021-07-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonton', '0002_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
