# Generated by Django 3.2.7 on 2021-10-12 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0002_auto_20211008_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skills',
            old_name='jobs',
            new_name='job',
        ),
    ]
