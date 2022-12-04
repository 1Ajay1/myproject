# Generated by Django 4.1 on 2022-09-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_join_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join_us',
            name='password',
        ),
        migrations.AddField(
            model_name='join_us',
            name='resume',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='resume/'),
        ),
    ]