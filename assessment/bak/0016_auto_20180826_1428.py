# Generated by Django 2.0.7 on 2018-08-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0015_auto_20180825_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislike',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='like',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
