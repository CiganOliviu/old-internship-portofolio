# Generated by Django 3.0.8 on 2020-08-19 13:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainView', '0014_guestenvironmentdetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GuestEnvironmentDetails',
            new_name='GuestEnvironmentDetail',
        ),
    ]