from django import forms
from .models import BookComment,ArticleComment,VideoComment

class BookCommentForm(forms.ModelForm):
    class Meta:
        model = BookComment
        fields = ['body']

class VideoCommentForm(forms.ModelForm):
    class Meta:
        model = VideoComment
        fields = ['body']

class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['body']
