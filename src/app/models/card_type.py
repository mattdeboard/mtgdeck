from django.db import models

class CardType(models.Model):
    artifact = models.BooleanField()
    conspiracy = models.BooleanField()
    creature = models.BooleanField()
    enchantment = models.BooleanField()
    instant = models.BooleanField()
    land = models.BooleanField()
    phenomenon = models.BooleanField()
    plane = models.BooleanField()
    planeswalker = models.BooleanField()
    scheme = models.BooleanField()
    sorcery = models.BooleanField()
    tribal = models.BooleanField()
    vanguard = models.BooleanField()
