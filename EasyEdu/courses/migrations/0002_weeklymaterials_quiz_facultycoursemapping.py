# Generated by Django 4.2.3 on 2023-08-12 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyMaterials',
            fields=[
                ('week', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('week_no', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('videos_link', models.CharField(max_length=1000)),
                ('slides_link', models.CharField(max_length=1000)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.faculty')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.coursesections')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('quiz_no', models.IntegerField(default=0)),
                ('quiz_link', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.faculty')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.coursesections')),
            ],
        ),
        migrations.CreateModel(
            name='FacultyCourseMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.faculty')),
                ('quizs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.quiz')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.coursesections')),
                ('weeks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.weeklymaterials')),
            ],
        ),
    ]
