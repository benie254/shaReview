# Generated by Django 4.0.5 on 2022-06-12 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0004_alter_contact_phone_alter_project_caption_a_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='caption_b',
            new_name='short_description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='caption_a',
        ),
    ]
