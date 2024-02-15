from django.test import TestCase

from ....models import Music, Artist

def create_artist(name):
    return Artist.objects.create(name=name)

def create_music(name, artist):
    return Music.objects.create(name=name, artist=artist)

class MusicModelTest(TestCase):
    def test_music_name(self):
        music_name = 'Something'
        music = create_music(music_name, create_artist("The Beatles"))
        self.assertEqual(music.name, music_name)

    def test_music_artist_name(self):
        music_name = 'Something'
        artist_name = 'The Beatles'
        artist = create_artist(artist_name)
        music = create_music(music_name, artist)
        self.assertEqual(music.artist.name, artist_name)

    def test_music_to_string(self):
        music_name = 'Something'
        artist_name = 'The Beatles'
        artist = create_artist(artist_name)
        music = create_music(music_name, artist)
        expected = artist_name + ' - ' + music_name
        self.assertEqual(str(music), expected)
