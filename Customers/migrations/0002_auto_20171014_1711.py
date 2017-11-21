# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='agreement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Customers.Agreement'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='ile_kat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='ile_prec',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='ile_satelit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='ile_sidewide',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='ile_spons',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='ile_wiz',
            field=models.IntegerField(default=0),
        ),
    ]
