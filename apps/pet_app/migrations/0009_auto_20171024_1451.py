# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 21:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet_app', '0008_auto_20171024_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='user',
            new_name='owner',
        ),
    ]
