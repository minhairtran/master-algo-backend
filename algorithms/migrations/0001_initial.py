# Generated by Django 2.2 on 2020-05-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('subtitle', models.TextField()),
                ('image', models.FileField(upload_to='images/')),
            ],
        ),
    ]