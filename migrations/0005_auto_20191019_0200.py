# Generated by Django 2.2.5 on 2019-10-19 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0004_auto_20191019_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='id_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.country'),
        ),
    ]
