# Generated by Django 3.2.4 on 2021-07-17 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nonton', '0003_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='playlist',
            field=models.CharField(default='True Story', max_length=225),
        ),
    ]
