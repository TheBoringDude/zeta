# Generated by Django 3.1.2 on 2020-11-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20201105_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='description',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]