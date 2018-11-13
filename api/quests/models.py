from __future__ import unicode_literals
from users.models import UserPlayer
from itens.models import Iten
from django.db import models


class Quests(models.Model):
    title = models.CharField(max_length=80, blank=False)
    description = models.TextField()
    reward_xp = models.IntegerField(blank=False)
    reward_score = models.IntegerField(blank=False)
    reward_iten = models.OneToOneField(Iten, on_delete=models.CASCADE)
    url = models.URLField()
    is_activated = models.BooleanField()
    creator = models.ForeignKey(UserPlayer, on_delete=models.CASCADE)