# Generated by Django 3.0.7 on 2020-07-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]