from ..models import Music, Artist
from ..serializers import ArtistSerializer
from rest_framework import serializers

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'name', 'artist']