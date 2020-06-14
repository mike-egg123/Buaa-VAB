from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

class ArticleColumn(models.Model):
    title = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Article(models.Model):
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 标题
    title = models.CharField(max_length=100)
    # 帖子内容
    body = models.TextField()
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)
    # 浏览次数
    total_views = models.PositiveIntegerField(default=0)
    # 点赞数
    likes = models.PositiveIntegerField(default=0)
    # 设置外键
    column = models.ForeignKey(ArticleColumn,null=True,blank=True,
                               on_delete=models.CASCADE,related_name='article')
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title