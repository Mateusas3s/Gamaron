# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import Group, User
from avatar.models import Avatar

from django.db import models


class UserPlayer(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        xp = models.IntegerField(blank=False)
        score_season = models.IntegerField(blank=False)
        avatar = models.ManyToManyField(Avatar)
