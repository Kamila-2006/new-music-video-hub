from django.db import models


class Track(models.Model):
    character = models.CharField(max_length=100, default='anonym')
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='tracks_images/')
    character_image = models.ImageField(upload_to='characters_images/')
    audio_file = models.FileField(upload_to='tracks_audio/')