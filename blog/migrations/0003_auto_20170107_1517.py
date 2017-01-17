# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-07 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170103_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='country',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Strana'),
        ),
    ]
