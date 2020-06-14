from django.urls import re_path, path
from django.conf.urls import url
from Usergroup import views

app_name = 'Usergroup'

urlpatterns = [
    path('', views.showGroup, name='showGroup'),
    path('<int:id>',views.GroupDetail, name='Groupdetail'),
    path('create',views.GroupCreate.as_view(), name='GroupCreate'),
    path('mygroup',views.MyGroupList,name='MyGroups'),
    path('join/<int:id>',views.JoinGroup,name='JoinGroup'),
    path('exit/<int:id>',views.ExitGroup,name='ExitGroup'),
    path('agreeAsk/<int:id>/',views.AgreeAsk,name='AgreeAsk'),
    path('refuseAsk/<int:id>/',views.RefuseAsk,name='RefuseAsk'),
    path('topArticle/<int:id>/<int:article_id>',views.topArticle,name='topArtilce'),
]
