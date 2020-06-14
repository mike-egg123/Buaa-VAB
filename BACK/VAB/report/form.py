from django import forms
from .models import BookCommentReport,ArticleCommentReport,VideoCommentReport

class BookCommentReportForm(forms.ModelForm):
    class Meta:
        model = BookCommentReport
        fields = ['reason']

class VideoCommentReportForm(forms.ModelForm):
    class Meta:
        model = VideoCommentReport
        fields = ['reason']

class ArticleCommentReportForm(forms.ModelForm):
    class Meta:
        model = ArticleCommentReport
        fields = ['reason']