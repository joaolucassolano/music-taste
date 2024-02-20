from django.db import models
from .artist import Artist

class Music(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.artist) + " - " + self.name
    
    def get_reviews(self):
        return self.review_set.all()