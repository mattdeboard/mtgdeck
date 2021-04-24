from django.db import models
from django.contrib.postgres.fields import ArrayField
from . import card_type, color_identity, converted_mana_cost

COLOR_IDENTITY_CHOICES = [
    ("B", "Black"),
    ("G", "Green"),
    ("R", "Red"),
    ("U", "Blue"),
    ("W", "White"),
]


CARD_TYPE_CHOICES = [
    ('AR', 'ARTIFACT'),
    ('CO', 'CONSPIRACY'),
    ('CR', 'CREATURE'),
    ('EN', 'ENCHANTMENT'),
    ('IN', 'INSTANT'),
    ('LA', 'LAND'),
    ('PH', 'PHENOMENON'),
    ('PL', 'PLANE'),
    ('PL', 'PLANESWALKER'),
    ('SC', 'SCHEME'),
    ('SO', 'SORCERY'),
    ('TR', 'TRIBAL'),
    ('AN', 'AVANGUARD')
]



class Card(models.Model):
    name = models.CharField(max_length=200)
    color_identity = color_identity.ColorIdentity()
    converted_mana_cost = converted_mana_cost.ConvertedManaCost()
    legalities = models.JSONField()
    art = models.URLField()
    supertype = models.CharField(max_length=500)
    card_type = card_type.CardType()

