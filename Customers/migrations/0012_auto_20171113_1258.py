# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-13 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0011_auto_20171106_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Do zrobienia', 'Do zrobienia'), ('W trakcie - u klienta', 'W trakcie - u klienta'), ('W trakcie - Gebuko', 'W trakcie - Gebuko'), ('Zrobione', 'Zrobione')], default='d', max_length=30),
        ),
    ]
