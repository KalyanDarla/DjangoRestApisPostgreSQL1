# Generated by Django 4.2.3 on 2023-08-02 08:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 8, 2, 8, 4, 51, 170462, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
