from ..models import Music
from ..serializers import ArtistSerializer
from rest_framework import serializers

class MusicSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)

    class Meta:
        model = Music
        fields = ['id', 'name', 'artist']