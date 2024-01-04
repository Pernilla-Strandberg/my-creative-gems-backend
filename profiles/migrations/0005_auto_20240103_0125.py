# Generated by Django 3.2.23 on 2024-01-03 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20240102_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='content_social',
        ),
        migrations.AddField(
            model_name='profile',
            name='content_social_facebook',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='content_social_tiktok',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='content_social_twitter',
            field=models.TextField(blank=True),
        ),
    ]