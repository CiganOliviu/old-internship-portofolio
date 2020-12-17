# Generated by Django 3.0.8 on 2020-09-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainView', '0019_auto_20200917_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guestenvironmentdetail',
            name='position',
        ),
        migrations.AddField(
            model_name='confirmanswer',
            name='position',
            field=models.CharField(choices=[('Guest', 'Guest'), ('Bridesmaid', 'Bridesmaid'), ('Groomsmen', 'Groomsmen'), ('Godparent', 'Godparent'), ('Parent', 'Parent'), ('Husband', 'Husband'), ('Wife', 'Wife')], default=0, max_length=25),
        ),
    ]