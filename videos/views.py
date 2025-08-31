from django.shortcuts import render, get_object_or_404
from .models import Video


def video_list(request):
    videos = Video.objects.all()
    ctx = {'videos': videos}
    return render(request, 'videos/video-list.html', ctx)

def video_detail(request, video_id):
    video = get_object_or_404(Video, video_id)
    ctx = {'video': video}
    return render(request, 'videos/video-detail.html', ctx)