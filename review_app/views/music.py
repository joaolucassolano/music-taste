from django.http import Http404

from ..models import Music
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import MusicSerializer

class MusicList(APIView):
    """
    List all musics or create a new music.
    """
    def get(self, request, format=None):
        musics = Music.objects.all()
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MusicDetail(APIView):
    """
    Retrieve, update or delete a music intance.
    """
    def get_object(self, pk):
        try:
            return Music.objects.get(pk=pk)
        except Music.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        music = self.get_object(pk)
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
