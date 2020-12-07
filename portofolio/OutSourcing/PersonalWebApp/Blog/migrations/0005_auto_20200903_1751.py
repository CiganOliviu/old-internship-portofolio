# Generated by Django 3.0.8 on 2020-09-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20200903_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='introduction',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_content_four',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_content_one',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_content_three',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_content_two',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_title_four',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_title_one',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_title_three',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_title_two',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]