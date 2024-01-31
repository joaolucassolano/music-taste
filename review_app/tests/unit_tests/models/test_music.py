from django.test import TestCase

from ....models import Music, Artist

def create_artist(name):
    return Artist.objects.create(name=name)

def create_music(name, artists=None):
    music = Music.objects.create(name=name)
    if artists is not None:
        for artist in artists:
            music.artists.add(artist)
    return music

class MusicModelTest(TestCase):
    def test_music_name(self):
        music_name = 'Something'
        music = create_music(music_name)
        self.assertEqual(music.name, music_name)

    def test_music_with_one_artist(self):
        music_name = 'Something'
        artist_name = 'The Beatles'
        artist = create_artist(artist_name)
        music = create_music(music_name, [artist])
        expected_music_artists = [artist]
        music_artists = list(music.artists.all())
        self.assertEqual(music_artists, expected_music_artists)

    def test_music_with_more_than_one_artits(self):
        music_name = 'Get Lucky'
        artist1_name = 'Daft Punk'
        artist2_name = 'Pharrell Willians'
        artist1 = create_artist(artist1_name)
        artist2 = create_artist(artist2_name)
        music = create_music(music_name, [artist1, artist2])
        expected_music_artists = [artist1, artist2]
        music_artists = list(music.artists.all())
        self.assertEqual(music_artists, expected_music_artists)

    def test_music_to_string_with_one_artist(self):
        music_name = 'Something'
        artist_name = 'The Beatles'
        artist = create_artist(artist_name)
        music = create_music(music_name, [artist])
        expected_music_to_string = artist_name + ' - ' + music_name
        self.assertEqual(str(music), expected_music_to_string)

    def test_music_to_string_with_more_than_one_artits(self):
        music_name = 'Get Lucky'
        artist1_name = 'Daft Punk'
        artist2_name = 'Pharrell Willians'
        artist1 = create_artist(artist1_name)
        artist2 = create_artist(artist2_name)
        artists = [artist1, artist2]
        music = create_music(music_name, artists)
        expected_music_to_string = ', '.join(str(artist) for artist in artists) + ' - ' + music_name
        self.assertEqual(str(music), expected_music_to_string)
