from django.db import models
from django.contrib.auth.models import User
from Books.models import Book
from Videos.models import Video
from article.models import Article
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel,TreeForeignKey

# 图书评论
class BookComment(models.Model):
    likes = models.PositiveIntegerField(default=0)

    hates = models.PositiveIntegerField(default=0)

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,# 联级删除
        related_name='Bookcomments'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Bookcomments'
    )

    body = RichTextField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]

# 影视评论
class VideoComment(models.Model):
    likes = models.PositiveIntegerField(default=0)

    hates = models.PositiveIntegerField(default=0)

    video = models.ForeignKey(
        Video,
        on_delete=models.CASCADE,# 联级删除
        related_name='Videocomments'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Videocomments'
    )

    body = RichTextField()
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body[:20]


# 帖子评论(可多级回复)
class ArticleComment(MPTTModel):
    likes = models.PositiveIntegerField(default=0)

    hates = models.PositiveIntegerField(default=0)

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='Articlecomments'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Aticlecomments'
    )

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    reply_to = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replyers'
    )

    canbeseen = models.BooleanField(default=True)
    body = RichTextField()
    created = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['created']
    def __str__(self):
        return self.body[:20]
