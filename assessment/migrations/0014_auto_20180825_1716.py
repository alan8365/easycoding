# Generated by Django 2.0.7 on 2018-08-25 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0013_comment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='ass_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assessment.AssessmentCode'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assessment.Comment'),
        ),
    ]
