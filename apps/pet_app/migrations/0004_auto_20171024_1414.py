# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet_app', '0003_auto_20171024_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets_owned', to='login_app.User'),
        ),
    ]