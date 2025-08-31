from django.urls import path
from . import views


app_name = 'tracks'

urlpatterns = [
    path('team/', views.character_list, name='team'),
    path('<int:character_id>/tracks/', views.character_tracks, name='tracks-list'),
    path('tracks/<int:track_id>/', views.music_detail, name='track-detail'),
]