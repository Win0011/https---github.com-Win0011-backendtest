from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Artist, Song
from .serializers import ArtistSerializer, SongSerializer

class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [permissions.IsAdminUser()]

class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return []
        return [permissions.IsAdminUser()]

class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
