from django.db import models
from .music import Music

class Review(models.Model):
    rate = models.IntegerField()
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.music) + ": " + str(self.rate)
