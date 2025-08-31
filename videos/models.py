from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='videos_images/')
    file = models.FileField(upload_to='video_files/')