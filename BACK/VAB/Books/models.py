from django.db import models
from PIL import Image

# 书籍
class Book(models.Model):
    Book_name = models.CharField(max_length=100)
    Book_auth = models.CharField(max_length=100)
    Book_intro = models.TextField(max_length=10000)
    Book_img = models.ImageField(upload_to='img', null=True)
    def __str__(self):
        return "%d" % self.pk
