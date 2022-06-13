# Generated by Django 4.0.5 on 2022-06-13 17:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0009_profile_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='creator',
        ),
        migrations.AddField(
            model_name='profile',
            name='creator',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]