# Generated by Django 4.0.5 on 2022-06-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='published',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
