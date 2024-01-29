from django.db import models
from .music import Music

class Review(models.Model):
    rate = models.IntegerField()
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
