from django.db import models

class ConvertedManaCost(models.Model):
    red = models.IntegerField()
    black = models.IntegerField()
    white = models.IntegerField()
    green = models.IntegerField()
    blue = models.IntegerField()
    colorless = models.IntegerField()

    class Meta:
      verbose_name_plural = "Converted Mana Costs"