# Generated by Django 3.0.8 on 2020-09-19 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0005_auto_20200919_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pastevent',
            old_name='event_slug',
            new_name='past_event_slug',
        ),
    ]