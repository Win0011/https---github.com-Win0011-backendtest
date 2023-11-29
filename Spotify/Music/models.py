
from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='artist_images/')
    Age = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=200)
    duration = models.DurationField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='song_images/')
    other_artists = models.ManyToManyField(Artist, related_name='featured_songs', blank=True)
    release_date = models.DateField()

    def __str__(self):
        return self.title
