# Generated by Django 2.2.5 on 2019-10-19 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopping',
            name='shopping_date',
            field=models.CharField(max_length=100),
        ),
    ]
