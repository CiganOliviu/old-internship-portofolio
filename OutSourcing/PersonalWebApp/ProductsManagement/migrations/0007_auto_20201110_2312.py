# Generated by Django 3.0.8 on 2020-11-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductsManagement', '0006_activeworkingproduct_percent_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='activeworkingproduct',
            name='active_working_product_slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='finishedproduct',
            name='finished_product_slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='plannedproduct',
            name='planned_product_slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
    ]
