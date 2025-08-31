from django.urls import path
from . import views


app_name = 'videos'

urlpatterns = [
    path('list/', views.video_list, name='video-list'),
    path('<int:video_id>/detail/', views.video_detail, name='video-detail'),
]