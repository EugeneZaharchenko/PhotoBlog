# Generated by Django 2.2.4 on 2019-08-24 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190816_0532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
