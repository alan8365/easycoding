# Generated by Django 2.0.2 on 2018-04-16 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessment',
            name='assessment_answer',
        ),
    ]