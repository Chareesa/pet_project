# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('pet_app', '0006_remove_pet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='user',
            field=models.ForeignKey(default='test', on_delete=django.db.models.deletion.CASCADE, related_name='pets_owned', to='login_app.User'),
        ),
    ]
