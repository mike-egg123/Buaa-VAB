from django.urls import re_path, path
from django.conf.urls import url
from Userprofile import views

app_name = 'Userprofile'

urlpatterns = [
    path('', views.loadHomepage, name='loadHomepage'),
    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('Userprofile/<int:id>/profile/', views.profile, name='profile'),
    path('Userprofile/<int:id>/profile/update/', views.profile_update, name='profile_update'),
    path('Userprofile/<int:id>/pwd_change/', views.pwd_change, name='pwd_change'),
    path('logout/', views.userlogout, name='logout'),
    path('registerajax/',views.registerajax,name='registerajax'),
    path('checkusers/',views.checkusers,name='checkusers'),
    path('checkusers_login/',views.checkusers_login,name='checkusers_login'),
    path('checkemail/',views.checkemail,name='checkemail'),
    path('checkpwd/',views.checkpwd,name='checkpwd'),
    path('checkpwd_login/', views.checkpwd_login, name='checkpwd_login'),
]
