# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0006_auto_20171020_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='start'),
        ),
    ]