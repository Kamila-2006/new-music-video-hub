from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='characters_images/')

    def __str__(self):
        return self.name


class Track(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='tracks_images/')
    audio_file = models.FileField(upload_to='tracks_audio/')

    def __str__(self):
        return self.title