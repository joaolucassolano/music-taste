from django.test import TestCase

from ....models import Music, Artist, Review

def create_review(rate, detail, music):
    return Review.objects.create(rate=rate, detail=detail, music=music)

def create_music(name, artist):
    return Music.objects.create(name=name, artist=artist)

def create_artist(name):
    return Artist.objects.create(name=name)

class ReviewModelTest(TestCase):
    def test_review_fields_without_detail(self):
        rate = 1
        detail = None
        music = create_music('Something', create_artist('The Beatles'))
        review = create_review(rate, detail, music)
        self.assertEqual(review.rate, rate)
        self.assertEqual(review.detail, detail)
        self.assertEqual(review.music, music)

    def test_review_fields_with_detail(self):
        rate = 1
        detail = 'Best music'
        music = create_music('Something', create_artist('The Beatles'))
        review = create_review(rate, detail, music)
        self.assertEqual(review.rate, rate)
        self.assertEqual(review.detail, detail)
        self.assertEqual(review.music, music)

    def test_review_to_string(self):
        rate = 1
        music = create_music('Something', create_artist('The Beatles'))
        review = create_review(rate, None, music)
        expected = str(music) + ': ' + str(rate)
        self.assertEqual(str(review), expected)
