# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-04-22 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import freenasUI.freeadmin.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0040_merge_20190403_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advanced',
            name='adv_periodic_notifyuser',
        ),
    ]
