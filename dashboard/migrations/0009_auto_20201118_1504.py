# Generated by Django 3.1.2 on 2020-11-18 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20201109_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='collection_id',
            field=models.BigIntegerField(unique=True),
        ),
    ]
