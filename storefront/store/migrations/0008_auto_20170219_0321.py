# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 02:21
from __future__ import unicode_literals

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20170219_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(),
        ),
    ]