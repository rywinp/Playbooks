from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def annotate_view(request):
    video = Video.objects.all().first()
    return render(request, "annotate.html", {"video": video})

def upload_view(request):
    if request.method == "POST":
        video = Video(video=request.FILES.get("video"))
        video.save()
    return render(request, "upload.html")

def showvideo(request):

    lastvideo= Video.objects.last()

    videofile= lastvideo.videofile


    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {'videofile': videofile,
              'form': form
              }
    
      
    return render(request, 'Blog/videos.html', context)


@login_required
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user  # Associate the video with the current user
            video.save()
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'video/uploadvid.html', {'form': form})
