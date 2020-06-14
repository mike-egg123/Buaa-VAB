from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('Video_name','Video_Country','Video_intro','Video_img','Video_tags','Video_column')