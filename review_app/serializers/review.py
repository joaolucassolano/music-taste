from ..models import Review
from ..serializers import MusicSerializer
from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
    music = MusicSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'rate', 'detail', 'music']