# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_remove_chechout_user_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chechout',
            name='user_details',
        ),
        migrations.DeleteModel(
            name='Chechout',
        ),
    ]
