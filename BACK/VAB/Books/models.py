from django.db import models
from django.urls import reverse
from PIL import Image
from django.utils import timezone
from taggit.managers import TaggableManager

# 书籍栏目
class BookColumn(models.Model):
    title = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# TODO:仿照article加入Meta，可以返回最新书籍
# 书籍
class Book(models.Model):
    Book_name = models.CharField(max_length=100)
    Book_auth = models.CharField(max_length=100)
    Book_intro = models.TextField(max_length=10000)
    Book_img = models.ImageField(upload_to='img', null=True)
    Book_total_views = models.PositiveIntegerField(default=0)
    Book_tags = TaggableManager(blank=True)
    Book_column = models.ForeignKey(BookColumn, null=True, blank=True,
                                    on_delete=models.CASCADE, related_name='book')

    def __str__(self):
        return self.Book_name

    def get_absolute_url(self):
        return reverse('Bookdetail', args=[self.id])
