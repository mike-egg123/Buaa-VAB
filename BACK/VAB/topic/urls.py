from django.urls import re_path, path
from django.conf.urls import url
from topic import views

app_name = 'topic'

urlpatterns = [
    path('',views.alltopics,name='alltopics'),
    path('topic-create/',views.createTopic,name='CreateTopic'),
    path('topic-detail/<int:id>/',views.topicDetail,name='TopicDetail'),
]