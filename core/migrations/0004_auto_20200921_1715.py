# Generated by Django 3.1.1 on 2020-09-21 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200921_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pnone',
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'teacher'), (3, 'admin')], primary_key=True, serialize=False),
        ),
    ]
