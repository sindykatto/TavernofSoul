# Generated by Django 3.2.8 on 2021-10-22 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='version',
            old_name='version_name',
            new_name='version',
        ),
    ]
