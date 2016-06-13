from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from .models import Artist
from .models import Album
from .serializers import ArtistSerializer
from .serializers import AlbumSerializer
from .serializers import SongSerializer


class ArtistsViewSet(viewsets.ModelViewSet):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumsViewSet(viewsets.ModelViewSet):

    serializer_class = AlbumSerializer

    def get_queryset(self):
        artist = get_object_or_404(Artist, pk=self.kwargs['artist_id'])
        return artist.albums

    def perform_create(self, serializer):
        artist = get_object_or_404(Artist, pk=self.kwargs['artist_id'])
        serializer.save(artist=artist)


class SongsViewSet(viewsets.ModelViewSet):

    serializer_class = SongSerializer

    def get_queryset(self):
        album = get_object_or_404(Album,
                                  pk=self.kwargs['album_id'],
                                  artist__pk=self.kwargs['artist_id'])
        return album.songs

    def perform_create(self, serializer):
        artist = get_object_or_404(Artist, pk=self.kwargs['artist_id'])
        album = get_object_or_404(artist.albums, pk=self.kwargs['album_id'])
        serializer.save(album=album)
