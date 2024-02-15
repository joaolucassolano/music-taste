from ..models import Music, Artist
from ..serializers import ArtistSerializer
from rest_framework import serializers

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'name', 'artist']

    def create(self, validated_data):
        music = Music.objects.create(**validated_data)
        return music
    
    def update(self, music, validated_data):
        super().update(music, validated_data)
        
        return music