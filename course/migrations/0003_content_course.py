# Generated by Django 2.0.7 on 2018-07-27 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_charpter'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
    ]
