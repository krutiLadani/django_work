# Generated by Django 2.1.1 on 2018-10-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_fee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='amount',
            field=models.FloatField(),
        ),
    ]
