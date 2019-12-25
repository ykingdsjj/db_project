# Generated by Django 3.0 on 2019-12-25 12:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_no', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'School',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_no', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=12)),
                ('gender', models.CharField(max_length=6)),
                ('age', models.IntegerField()),
                ('password', models.CharField(blank=True, max_length=100)),
                ('major', models.CharField(max_length=15, verbose_name='专业')),
                ('enrollmentDate', models.DateField(verbose_name='入学时间')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.School')),
            ],
            options={
                'db_table': 'Student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_no', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=2)),
                ('title', models.CharField(choices=[('Instructor', '讲师'), ('Assitant', '助理教授'), ('Associate', '副教授'), ('Professor', '教授')], default='Instructor', max_length=15)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.School')),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('account', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('character', models.CharField(choices=[('1', '学生'), ('2', '教师'), ('3', '教秘')], max_length=1)),
                ('x_no', models.CharField(max_length=12)),
                ('password', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'User',
            },
        ),
        migrations.CreateModel(
            name='SchoolAdmin',
            fields=[
                ('admin_no', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('admin_name', models.CharField(max_length=20)),
                ('password', models.CharField(blank=True, max_length=100)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.School', unique=True)),
            ],
            options={
                'db_table': 'SchoolAdmin',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_no', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('course_type', models.CharField(choices=[('ZYBX', '专业必修'), ('ZYXX', '专业选修')], max_length=4)),
                ('course_name', models.CharField(max_length=20)),
                ('course_score', models.PositiveIntegerField(default=0)),
                ('location', models.CharField(default='', max_length=15)),
                ('course_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('major', models.CharField(blank=True, max_length=15)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.School')),
            ],
            options={
                'db_table': 'Course',
            },
        ),
        migrations.CreateModel(
            name='TeacherCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(blank=True, max_length=15, verbose_name='学期')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.Course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.Teacher')),
            ],
            options={
                'db_table': 'TeacherCourse',
                'unique_together': {('teacher', 'course', 'semester')},
            },
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(blank=True, max_length=15, verbose_name='学期')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name='成绩')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qqa.Student')),
            ],
            options={
                'db_table': 'StudentCourse',
                'unique_together': {('student', 'course', 'semester')},
            },
        ),
    ]
