from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from Books.models import Book
from Videos.models import Video
from article.models import Article
from comment.models import BookComment,ArticleComment,VideoComment

# 举报图书评论
class BookCommentReport(models.Model):
    reporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='BookcommentReport'
    )

    Administrator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='BookcommentAdministrator',
    )

    bookcomment = models.ForeignKey(
        BookComment,
        on_delete=models.CASCADE,
        related_name='BookcommentReport'
    )

    reason = models.TextField(
        max_length=100
    )

    state = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reason


# 举报影视评论
class VideoCommentReport(models.Model):
    reporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='VideocommentReport'
    )

    Administrator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='VideocommentAdministrator',
    )

    videocomment = models.ForeignKey(
        VideoComment,
        on_delete=models.CASCADE,
        related_name='VideocommentReport'
    )

    reason = models.TextField(
        max_length=100
    )

    state = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reason


# 举报帖子评论
class ArticleCommentReport(models.Model):
    reporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ArticlecommentReport'
    )

    Administrator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ArticlecommentAdministrator',
    )

    articlecomment = models.ForeignKey(
        ArticleComment,
        on_delete=models.CASCADE,
        related_name='ArticlecommentReport'
    )

    reason = models.TextField(
        max_length=100
    )

    state = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reason