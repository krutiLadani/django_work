# Generated by Django 2.1.1 on 2018-10-09 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20181008_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
    ]
