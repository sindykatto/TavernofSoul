# Generated by Django 3.2.9 on 2021-11-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buffs', '0004_alter_buffs_applytime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buffs',
            name='id_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='buffs',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
