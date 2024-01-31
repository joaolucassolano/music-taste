from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name;

    def get_musics(self):
        return self.music_set.all()