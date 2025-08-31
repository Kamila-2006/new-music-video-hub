from django.shortcuts import render, get_object_or_404
from .models import Character, Track


def home(request):
    return render(request, 'index.html')

def character_list(request):
    characters = Character.objects.all()
    ctx = {'characters': characters}
    return render(request, 'tracks/characters.html', ctx)

def character_tracks(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    tracks = character.tracks.all()
    ctx = {
        'character': character,
        'tracks': tracks
    }
    return render(request, 'tracks/music-list.html', ctx)

def music_detail(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    ctx = {'track': track}
    return render(request, 'tracks/music-detail.html', ctx)