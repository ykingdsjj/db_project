# Generated by Django 2.2.6 on 2019-12-26 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qqa', '0002_auto_20191226_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooladmin',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='password',
        ),
    ]
