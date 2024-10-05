from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos', blank=True, null=True)
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption