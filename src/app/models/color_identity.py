from django.db import models

class ColorIdentity(models.Model):
    red = models.BooleanField()
    black = models.BooleanField()
    white = models.BooleanField()
    green = models.BooleanField()
    blue = models.BooleanField()

    def is_colorless(self):
      return self.red and self.black and self.white and self.green and self.blue

    class Meta:
        verbose_name_plural = "Color Identities"

