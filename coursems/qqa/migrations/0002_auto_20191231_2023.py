# Generated by Django 3.0 on 2019-12-31 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qqa', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentcourlas',
            old_name='semester',
            new_name='term',
        ),
        migrations.AlterUniqueTogether(
            name='studentcourlas',
            unique_together={('student_no', 'courlas_no', 'term')},
        ),
    ]
