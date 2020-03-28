from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.showBook),
    url(r'^(\d+)$', views.Bookdetail),
    url('upload', views.Bookupload),
]
