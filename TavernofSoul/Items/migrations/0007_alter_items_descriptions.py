# Generated by Django 3.2.9 on 2021-11-16 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0006_alter_items_id_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='descriptions',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
