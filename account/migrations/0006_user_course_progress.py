# Generated by Django 2.0.7 on 2018-08-06 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20180803_1115'),
        ('account', '0005_user_assess_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='course_progress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
    ]