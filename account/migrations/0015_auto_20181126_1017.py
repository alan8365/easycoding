# Generated by Django 2.0.7 on 2018-11-26 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20181122_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement_get',
            name='achievement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Achievement'),
        ),
    ]