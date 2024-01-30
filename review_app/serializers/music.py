from ..models import Music, Artist
from ..serializers import ArtistSerializer
from rest_framework import serializers

class MusicSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True)
    
    class Meta:
        model = Music
        fields = ['id', 'name', 'artists']

    def create(self, validated_data):
        artists_data = validated_data.pop('artists')
        music = Music.objects.create(**validated_data)
        for artist_data in artists_data:
            artist, _ = Artist.objects.get_or_create(**artist_data)
            music.artists.add(artist)
        return music
    
    def update(self, music, validated_data):
        artists_data = validated_data.pop('artists')
        music.artists.clear()
        for artist_data in artists_data:
            artist, _ = Artist.objects.get_or_create(**artist_data)
            music.artists.add(artist)
        super().update(music, validated_data)
        
        return music