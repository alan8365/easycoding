# Generated by Django 2.0.7 on 2018-09-10 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=0)),
                ('content', models.TextField(max_length=2100)),
                ('isTitle', models.BooleanField(default=False)),
                ('isText', models.BooleanField(default=False)),
                ('isCode', models.BooleanField(default=False)),
                ('isTable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lesson', models.PositiveIntegerField()),
                ('chapter', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='wiki',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wiki.Wiki'),
        ),
    ]