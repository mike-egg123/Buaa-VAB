from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('Book_name','Book_auth','Book_intro','Book_img','Book_column','Book_tags')