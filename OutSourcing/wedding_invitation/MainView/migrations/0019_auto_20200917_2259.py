# Generated by Django 3.0.8 on 2020-09-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainView', '0018_auto_20200917_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestenvironmentdetail',
            name='position',
            field=models.CharField(choices=[('Guest', 'Guest'), ('Bridesmaid', 'Bridesmaid'), ('Groomsmen', 'Groomsmen'), ('Godparent', 'Godparent'), ('Parent', 'Parent'), ('Husband', 'Husband'), ('Wife', 'Wife')], default=0, max_length=25),
        ),
    ]
