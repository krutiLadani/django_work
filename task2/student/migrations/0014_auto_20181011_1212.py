# Generated by Django 2.1.1 on 2018-10-11 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20181010_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='uuid',
            field=models.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
    ]