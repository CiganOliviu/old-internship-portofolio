# Generated by Django 3.0.8 on 2020-10-22 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ClientsManagement', '0008_clientinfo_number_of_projects_in_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.TextField()),
                ('list_of_functionalities', models.TextField()),
                ('type', models.CharField(choices=[('Presentation WebSite', 'Presentation WebSite'), ('WebApp', 'Webapp'), ('Mobile App', 'Mobile App')], max_length=100)),
                ('project_status', models.CharField(choices=[('Waiting for Response', 'Waiting for Response'), ('Refused', 'Refused'), ('Accepted', 'Accepted')], default='Processing', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='ClientInfo',
            new_name='ClientsDetail',
        ),
        migrations.RenameModel(
            old_name='FeedBack',
            new_name='ClientsFeedBack',
        ),
        migrations.RenameModel(
            old_name='DirectClientContact',
            new_name='MessagesToClient',
        ),
        migrations.DeleteModel(
            name='AskProject',
        ),
    ]