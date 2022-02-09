# Generated by Django 3.2.6 on 2022-01-24 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Buffs', '0005_auto_20211116_1000'),
        ('Monsters', '0007_auto_20211116_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buff_Skill_Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chance', models.FloatField()),
                ('duration', models.FloatField()),
                ('buff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Buffs.buffs')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Monsters.skill_monster')),
            ],
        ),
    ]