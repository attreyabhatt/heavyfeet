# Generated by Django 5.1.4 on 2024-12-22 04:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailytasks', '0002_rename_author_usertask_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertask',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
