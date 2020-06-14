from django.conf.urls import url
from django.urls import path
from . import views
from Books.views import Bookupdload

urlpatterns = [
    path('', views.showBook, name='showBook'),
    path('<int:id>', views.Bookdetail, name='Bookdetail'),
    path('upload', views.Bookupdload.as_view(), name='Bookupload'),
]
