# Generated by Django 2.1.1 on 2018-10-15 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_auto_20181015_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
