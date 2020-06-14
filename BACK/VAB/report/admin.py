from django.contrib import admin
from .models import BookCommentReport,VideoCommentReport,ArticleCommentReport

admin.site.register(BookCommentReport)
admin.site.register(VideoCommentReport)
admin.site.register(ArticleCommentReport)

