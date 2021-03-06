# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-01 04:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20180501_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='chechout',
            name='user_details',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chechout',
            name='user_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
