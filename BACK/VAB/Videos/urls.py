from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showVideo, name='showVideo'),
    path('<int:id>', views.Videodetail, name='Videodetail'),
    path('upload', views.Videoupdload.as_view(), name='Videoupload'),
]
