# Generated by Django 3.2.5 on 2021-07-28 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210724_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processordetail',
            name='clock_max_speed',
        ),
        migrations.RemoveField(
            model_name='processordetail',
            name='clock_min_speed',
        ),
    ]
