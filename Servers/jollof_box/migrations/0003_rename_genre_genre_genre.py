# Generated by Django 4.1.6 on 2023-11-23 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jollof_box', '0002_rename_download_link_episode_download_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='Genre',
            new_name='genre',
        ),
    ]