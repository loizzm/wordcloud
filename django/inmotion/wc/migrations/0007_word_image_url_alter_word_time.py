# Generated by Django 4.2.3 on 2023-08-15 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wc', '0006_word_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='word',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 15, 20, 15, 37, 250289)),
        ),
    ]
