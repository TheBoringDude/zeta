# Generated by Django 3.1.2 on 2020-11-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20201104_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='collection_id',
            field=models.IntegerField(default=540148039789900295974028087228, unique=True),
        ),
    ]