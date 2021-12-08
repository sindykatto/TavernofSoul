# Generated by Django 3.2.7 on 2021-10-08 01:24

from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Monsters', '0001_initial'),
        ('Items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(db_index=True, max_length=20)),
                ('id_name', models.CharField(max_length=30)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('has_cm', models.BooleanField(default=False)),
                ('has_warp', models.BooleanField(default=False)),
                ('level', models.IntegerField(default=-1)),
                ('max_elite', models.IntegerField(default=-1)),
                ('max_hate', models.IntegerField(default=-1)),
                ('star', models.IntegerField(default=-1)),
                ('type', models.CharField(max_length=10)),
                ('map_link', django_mysql.models.ListCharField(models.CharField(max_length=20), max_length=220, size=10)),
            ],
        ),
        migrations.CreateModel(
            name='Map_NPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positions', django_mysql.models.ListCharField(models.CharField(max_length=20), max_length=220, size=10)),
                ('population', models.IntegerField()),
                ('time_respawn', models.FloatField()),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Maps.maps')),
                ('monster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monsters.monsters')),
            ],
        ),
        migrations.CreateModel(
            name='Map_Item_Spawn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positions', django_mysql.models.ListCharField(models.CharField(max_length=20), max_length=220, size=10)),
                ('population', models.IntegerField()),
                ('time_respawn', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Items.items')),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Maps.maps')),
            ],
        ),
        migrations.CreateModel(
            name='Map_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chance', models.FloatField(blank=True, default=0, null=True)),
                ('qty_max', models.IntegerField(blank=True, default=0, null=True)),
                ('qty_min', models.IntegerField(blank=True, default=0, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Items.items')),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Maps.maps')),
            ],
        ),
    ]
