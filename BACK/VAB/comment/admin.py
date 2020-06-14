from django.contrib import admin
from .models import BookComment,ArticleComment,VideoComment

admin.site.register(BookComment)
admin.site.register(ArticleComment)
admin.site.register(VideoComment)