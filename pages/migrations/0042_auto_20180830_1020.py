# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-30 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0041_auto_20180713_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Раздел сайта', 'verbose_name_plural': 'Разделы сайта'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Страница', 'verbose_name_plural': 'Страницы'},
        ),
        migrations.RemoveField(
            model_name='offers',
            name='offer_price',
        ),
        migrations.AlterField(
            model_name='offers',
            name='offer_subtags',
            field=models.ManyToManyField(blank=True, to='pages.Subtags', verbose_name='Метки'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='offer_url',
            field=models.CharField(max_length=250, verbose_name='урл страницы'),
        ),
    ]