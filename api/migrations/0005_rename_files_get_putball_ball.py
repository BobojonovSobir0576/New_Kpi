# Generated by Django 4.2.6 on 2023-10-31 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_ball_putball_files_get'),
    ]

    operations = [
        migrations.RenameField(
            model_name='putball',
            old_name='files_get',
            new_name='ball',
        ),
    ]
