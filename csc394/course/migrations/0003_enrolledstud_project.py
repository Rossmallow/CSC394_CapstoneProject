# Generated by Django 2.2.6 on 2019-10-22 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='enrolledStud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.IntegerField()),
                ('firstName', models.CharField(max_length=250)),
                ('lastName', models.CharField(max_length=250)),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('members', models.ManyToManyField(to='course.enrolledStud')),
            ],
        ),
    ]
