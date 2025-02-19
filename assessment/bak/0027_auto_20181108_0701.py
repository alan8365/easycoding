# Generated by Django 2.0.7 on 2018-11-08 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0026_assessment_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('content', models.TextField(max_length=2100)),
                ('isTitle', models.BooleanField(default=False)),
                ('isText', models.BooleanField(default=False)),
                ('isCode', models.BooleanField(default=False)),
                ('isImage', models.BooleanField(default=False)),
                ('isLink', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='content',
        ),
        migrations.AddField(
            model_name='content',
            name='assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assessment.Assessment'),
        ),
    ]
