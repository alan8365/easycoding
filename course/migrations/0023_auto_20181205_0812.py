# Generated by Django 2.0.7 on 2018-12-05 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_content_istable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fill',
            name='content',
            field=models.TextField(max_length=2000),
        ),
    ]
