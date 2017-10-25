# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

class Pet(models.Model):
    pet_name = models.CharField(max_length = 50)
    pet_type = models.CharField(max_length = 25)
    owner = models.ForeignKey(User, related_name="pets_owned", default=None)
    #Pet model, links to User table from login_app
