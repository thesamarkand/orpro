# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-18 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20180118_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]