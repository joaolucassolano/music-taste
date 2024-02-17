from django.db import models
from .music import Music

class Review(models.Model):
    rate = models.IntegerField()
    detail = models.CharField(max_length=1000, default=None, blank=True, null=True)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.music) + ": " + str(self.rate)
