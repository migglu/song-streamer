from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=80, unique=True)


class Album(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(
        Artist, related_name='albums', on_delete=models.PROTECT)


class Song(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    album = models.ForeignKey(
        Album, related_name='songs', on_delete=models.PROTECT)

    class Meta:
        ordering = ['order']

    @property
    def artist(self):
        return self.album.artist
