# Generated by Django 3.0 on 2019-12-25 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qqa', '0008_auto_20191221_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentcourse',
            name='teacher',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_no',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_no',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
    ]
