# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-03-05 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studCourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Documents',
            new_name='Document',
        ),
        migrations.RenameModel(
            old_name='Subscribes',
            new_name='Subscribe',
        ),
    ]
