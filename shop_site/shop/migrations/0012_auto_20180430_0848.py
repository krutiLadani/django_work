# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20180430_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chechout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Profile'),
        ),
    ]