# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20180509_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
