from django.db import models
from .artist import Artist

class Music(models.Model):
    name = models.CharField(max_length=200)
    artists = models.ManyToManyField(Artist)

    def getArtists(self):
        return ", ".join([a.name for a in self.artists.all()])

    def __str__(self):
        return self.getArtists() + " - " + self.name