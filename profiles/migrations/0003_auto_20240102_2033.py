# Generated by Django 3.2.23 on 2024-01-02 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20240101_2355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='facebook_url',
            new_name='facebookUrl',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='tiktok_url',
            new_name='tiktokUrl',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='twitter_url',
            new_name='twitterUrl',
        ),
    ]