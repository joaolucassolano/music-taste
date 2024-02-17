from django.db import models
from .music import Music
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    rate = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    detail = models.CharField(max_length=1000, default=None, blank=True, null=True)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.music) + ": " + str(self.rate)
