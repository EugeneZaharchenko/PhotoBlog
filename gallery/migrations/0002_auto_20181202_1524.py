# Generated by Django 2.1.3 on 2018-12-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='country',
            field=models.ForeignKey(default=None, on_delete=None, to='gallery.Strana'),
        ),
    ]
