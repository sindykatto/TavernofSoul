# Generated by Django 3.2.9 on 2021-11-16 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0011_alter_items_id_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipments',
            name='type_attack',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='equipments',
            name='type_equipment',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]