# Generated by Django 5.1.4 on 2024-12-21 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailytasks', '0003_rename_task_usertask'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertask',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
