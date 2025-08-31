from django.contrib import admin
from .models import Character, Track


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name']


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'artist',
        'album',
        'genre',
        'release_date',
        'cover_image',
        'audio_file'
    ]
    list_filter = ['character', 'artist', 'album', 'genre']