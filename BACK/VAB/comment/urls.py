from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('post-Bookcomment/<int:id>/',views.post_Bookcomment,name='post_Bookcomment'),
    path('post-Videocomment/<int:id>/',views.post_Videocomment,name='post_Videocomment'),
    path('post-Articlecomment/<int:article_id>/',views.post_Articlecomment,name='post_Articlecomment'),
    path('post-Articlecomment/<int:article_id>/<int:parent_comment_id>',views.post_Articlecomment,name='comment_reply'),
    path('delete-Bookcomment/<int:id>/',views.delete_Bookcomment,name='delete_Bookcomment'),
    path('delete-Videocomment/<int:id>/',views.delete_Videocomment,name='delete_Videocomment'),
    path('delete-Articlecomment/<int:id>/',views.delete_Articlecomment,name='delete_Articlecomment'),
    path('like-Bookcomment/<int:id>/',views.like_Bookcomment,name='like_Bookcomment'),
    path('like-Videocomment/<int:id>/',views.like_Videocomment,name='like_Videocomment'),
    path('like-Articlecomment/<int:id>/',views.like_Articlecomment,name='like_Articlecomment'),
    path('unlike-Bookcomment/<int:id>/',views.unlike_Bookcomment,name='unlike_Bookcomment'),
    path('unlike-Videocomment/<int:id>/',views.unlike_Videocomment,name='unlike_Videocomment'),
    path('unlike-Articlecomment/<int:id>/',views.unlike_Articlecomment,name='unlike_Articlecomment'),
]