# Generated by Django 4.0.5 on 2022-06-13 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0010_remove_profile_creator_profile_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='creator',
            new_name='creator_id',
        ),
    ]