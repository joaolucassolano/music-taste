from django.db import models
from .artist import Artist

class Music(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    artists = models.ManyToManyField(Artist)