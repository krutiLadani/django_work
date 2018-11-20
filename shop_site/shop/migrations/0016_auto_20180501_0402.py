# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-01 04:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0015_auto_20180430_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, max_length=500)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('zip', models.CharField(blank=True, max_length=30, null=True)),
                ('phone_no', models.CharField(max_length=13)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='chechout',
            name='address',
        ),
        migrations.RemoveField(
            model_name='chechout',
            name='city',
        ),
        migrations.RemoveField(
            model_name='chechout',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='chechout',
            name='state',
        ),
        migrations.RemoveField(
            model_name='chechout',
            name='user',
        ),
        migrations.RemoveField(
            model_name='chechout',
            name='zip',
        ),
        migrations.AddField(
            model_name='chechout',
            name='chechout',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Profile'),
            preserve_default=False,
        ),
    ]