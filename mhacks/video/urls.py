
from django.urls import path
from . import views

urlpatterns = [
    path("", views.annotate_view, name="view_videos"),
    path("upload/", views.upload_video, name="upload_video"),
]

