# Generated by Django 2.2.6 on 2019-10-30 21:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_todoitem_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]
