from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    topic = models.CharField(max_length=100, blank=True)
    body = models.TextField(max_length=1000,blank=True)
    allcount = models.PositiveIntegerField(default=0)
    topicimg = models.ImageField(upload_to='topicimg/', null=True)

    def __str__(self):
        return self.topic