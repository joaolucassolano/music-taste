from django.http import HttpRequest, Http404

from .models import Artist, Music, Review
from rest_framework import views, status
from rest_framework.response import Response

from .serializers import ArtistSerializer, MusicSerializer

class ArtistList(views.APIView):
    """
    List all artists or create a new artist.
    """
    def get(self, request, format=None):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ArtistDetail(views.APIView):
    """
    Retrieve, update or delete a artist instance.
    """
    def get_object(self, pk):
        try:
            return Artist.objects.get(pk=pk)
        except Artist.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        artist = self.get_object(pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        artist = self.get_object(pk)
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        artist = self.get_object(pk)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

