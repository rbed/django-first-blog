# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 19:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='text',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default='admin', on_delete=django.db.models.deletion.SET_DEFAULT, to='blog.Author'),
        ),
    ]
