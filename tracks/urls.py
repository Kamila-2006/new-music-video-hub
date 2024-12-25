from django.urls import path
from . import views

app_name = 'tracks'

urlpatterns = [
    path('list/', views.music_list, name='music-list'),
    path('create/', views.music_create, name='music-create'),
    path('detail/<int:track_id>/', views.music_detail, name='music-detail'),
    path('update/<int:track_id>/', views.music_update, name='music-update'),
    path('delete/<int:track_id>/', views.music_delete, name='music-delete'),
]