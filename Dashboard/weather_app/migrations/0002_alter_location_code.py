# Generated by Django 3.2.5 on 2021-07-15 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='code',
            field=models.IntegerField(unique=True),
        ),
    ]