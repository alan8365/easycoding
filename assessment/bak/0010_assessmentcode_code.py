# Generated by Django 2.0.7 on 2018-08-03 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0009_auto_20180802_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessmentcode',
            name='code',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
