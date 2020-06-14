from django.urls import path
from . import views

urlpatterns = [
    path('',views.showArticle,name='showArticle'),
    path('article-detail/<int:id>/',views.ArticleDetail,name='ArticleDetail'),
    path('article-create/',views.ArticleCreate,name='ArticleCreate'),
    path('article-delete/<int:id>/',views.ArticleDelete,name='ArticleDelete'),
    path('article-update/<int:id>/',views.ArticleUpdate,name='ArticleUpdate'),
    path('increase-likes/<int:id>/',views.IncreaseLikesView.as_view(),name='increase_likes'),
    path('delete-group-post/<int:gid>/<int:id>/',views.GroupPostDelete,name='GroupDeletePost'),
]