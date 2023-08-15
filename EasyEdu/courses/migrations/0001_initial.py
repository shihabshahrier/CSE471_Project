# Generated by Django 4.2.3 on 2023-08-12 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('course_title', models.CharField(max_length=100)),
                ('course_credit', models.IntegerField(default=0)),
                ('course_description', models.TextField()),
                ('course_prerequisite', models.CharField(max_length=100)),
                ('course_department', models.CharField(max_length=100)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.org')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSections',
            fields=[
                ('section_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('section_capacity', models.IntegerField(default=0)),
                ('section_enrolled', models.IntegerField(default=0)),
                ('section_day', models.CharField(max_length=10)),
                ('section_start_time', models.TimeField()),
                ('section_end_time', models.TimeField()),
                ('section_room', models.CharField(max_length=10)),
                ('section_session', models.CharField(max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.faculty')),
            ],
        ),
    ]