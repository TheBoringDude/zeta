# Generated by Django 3.1.2 on 2020-11-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20201105_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='collection_id',
            field=models.IntegerField(unique=True),
        ),
    ]