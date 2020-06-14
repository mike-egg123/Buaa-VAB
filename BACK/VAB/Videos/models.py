from django.db import models
from django.urls import reverse
from PIL import Image
from django.utils import timezone
from taggit.managers import TaggableManager

# 影视栏目
class VideoColumn(models.Model):
    title = models.CharField(max_length=100,blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# 影视
class Video(models.Model):
    Video_name = models.CharField(max_length=200)
    Video_Country = models.CharField(max_length=500)
    Video_intro = models.TextField(max_length=10000)
    Video_img = models.ImageField(upload_to='img',null=True)
    Video_tags = TaggableManager(blank=True)
    Video_column = models.ForeignKey(VideoColumn, null=True, blank=True,
                                     on_delete=models.CASCADE, related_name='video')

    def __str__(self):
        return "%d" % self.pk
