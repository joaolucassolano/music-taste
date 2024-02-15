from django.test import TestCase
from ....models import Music, Artist

def create_artist(name):
    return Artist.objects.create(name=name)

def create_music(name, artist):
    music = Music.objects.create(name=name, artist=artist)
    return music

class ArtistModelTest(TestCase):
    def test_artist_name(self):
        artist_name = 'The Beatles'
        artist = create_artist(artist_name)
        self.assertEqual(artist.name, artist_name)

    def test_artist_to_string(self):
        artist_name = 'The Beatles'
        artist = create_artist(artist_name)
        self.assertEqual(str(artist), artist_name)

    def test_artist_with_one_music(self):
        artist_name = 'The Beatles'
        artist = create_artist(artist_name)
        music = create_music('Something', artist)
        expected_artist_musics = [music]
        artist_musics = list(artist.get_musics())
        self.assertEqual(artist_musics, expected_artist_musics)

    def test_artist_with_more_than_one_music(self):
        artist_name = 'The Beatles'
        artist = create_artist(artist_name)
        music1 = create_music('Something', artist)
        music2 = create_music('Hey Jude!', artist)
        expected_artist_musics = [music1, music2]
        artist_musics = list(artist.get_musics())
        self.assertEqual(artist_musics, expected_artist_musics)