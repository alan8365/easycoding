# Generated by Django 2.0.7 on 2018-11-22 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assessment', '0028_auto_20181122_0334'),
    ]

    operations = [
        migrations.CreateModel(
            name='HaveVoted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ass_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assessment.AssessmentCode')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='havevote',
            name='ass',
        ),
        migrations.RemoveField(
            model_name='havevote',
            name='ass_code',
        ),
        migrations.RemoveField(
            model_name='havevote',
            name='user',
        ),
        migrations.DeleteModel(
            name='HaveVote',
        ),
    ]
