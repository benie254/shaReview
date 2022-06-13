# Generated by Django 4.0.5 on 2022-06-13 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0012_remove_profile_creator_id_profile_creator_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='creator_id',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='creator_id',
            new_name='creator',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='project',
        ),
    ]
