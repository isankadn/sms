# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 05:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='lastname_name',
            new_name='last_name',
        ),
    ]
