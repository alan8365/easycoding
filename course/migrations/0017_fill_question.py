# Generated by Django 2.0.7 on 2018-11-05 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_content_isimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='fill',
            name='question',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
