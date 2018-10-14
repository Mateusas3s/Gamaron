# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import Group, User

from django.db import models

#
# class UserType(models.Model):
#     name = models.CharField(max_length=80, validators=[MinLengthValidator(5)],
#     blank=False, verbose_name="Name")

class UserPlayer(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        xp = models.IntegerField(blank=False)
        # type = models.ForeignKey(UserType, on_delete=models.CASCADE)
