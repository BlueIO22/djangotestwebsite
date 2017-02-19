# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20170219_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='reviewlink',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='var/www/media/'),
        ),
    ]