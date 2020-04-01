from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showBook, name='showBook'),
    path('<int:id>', views.Bookdetail, name='Bookdetail'),
    path('upload', views.Bookupload, name='Bookupload'),
]
