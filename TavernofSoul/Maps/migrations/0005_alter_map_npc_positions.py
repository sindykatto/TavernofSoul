# Generated by Django 3.2.9 on 2021-11-16 07:25

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('Maps', '0004_alter_map_npc_positions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map_npc',
            name='positions',
            field=django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=1050, size=20),
        ),
    ]
