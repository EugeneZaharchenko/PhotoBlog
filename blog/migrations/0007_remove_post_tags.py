# Generated by Django 2.2.4 on 2019-08-24 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]