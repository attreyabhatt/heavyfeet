# Generated by Django 5.1.4 on 2024-12-22 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailytasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertask',
            old_name='author',
            new_name='user',
        ),
    ]
