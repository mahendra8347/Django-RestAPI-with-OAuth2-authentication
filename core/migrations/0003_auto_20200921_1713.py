# Generated by Django 3.1.1 on 2020-09-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pnone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'student'), (2, 'teacher'), (3, 'admin'), (4, 'manager')], primary_key=True, serialize=False),
        ),
    ]
