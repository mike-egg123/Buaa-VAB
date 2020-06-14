from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from article.models import Article

class Usergroup(models.Model):
    # 小组名称
    groupname = models.CharField(max_length=100)

    # 组长
    groupMaster = models.ForeignKey(User, on_delete=models.CASCADE, related_name='groupmaster')

    # 多对多的小组成员
    members = models.ManyToManyField(User,related_name='members')

    # 小组管理员
    group_managers = models.ManyToManyField(User,related_name='managers')

    # 小组创建日期
    createdTime = models.DateTimeField(default=timezone.now)

    # 小组成员数量
    groupsize = models.IntegerField(default=1)

    # 小组头像
    group_img = models.ImageField(upload_to='groupimg', null=True)

    # 小组简介
    group_info = models.TextField(max_length=1000,blank=True)

    # 置顶帖子
    top_article = models.ForeignKey(
        Article,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
