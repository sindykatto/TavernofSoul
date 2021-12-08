# Generated by Django 3.2.7 on 2021-10-15 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='items',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Equipment_Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(db_index=True, max_length=30)),
                ('id_name', models.CharField(db_index=True, max_length=30)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('bonus2', models.CharField(db_index=True, max_length=100)),
                ('bonus3', models.CharField(db_index=True, max_length=100)),
                ('bonus4', models.CharField(db_index=True, max_length=100)),
                ('bonus5', models.CharField(db_index=True, max_length=100)),
                ('bonus6', models.CharField(db_index=True, max_length=100)),
                ('bonus7', models.CharField(db_index=True, max_length=100)),
                ('equipment', models.ManyToManyField(to='Items.Equipments')),
            ],
        ),
    ]
