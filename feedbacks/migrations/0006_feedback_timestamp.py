# Generated by Django 2.2 on 2020-05-09 10:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0005_feedback_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
