# Generated by Django 4.2.3 on 2023-08-14 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wc', '0005_alter_word_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 14, 13, 41, 21, 865173)),
        ),
    ]
