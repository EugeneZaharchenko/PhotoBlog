# Generated by Django 2.2.4 on 2019-09-01 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20190831_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blog.Post'),
        ),
    ]