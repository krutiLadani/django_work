# Generated by Django 2.1.1 on 2018-10-09 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20181009_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fee',
            name='fee_type',
        ),
    ]
