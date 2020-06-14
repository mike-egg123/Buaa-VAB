"""VAB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
import notifications.urls

urlpatterns = [
    # 用户管理
    path('admin/', admin.site.urls),

    # 图书管理
    path('book/', include('Books.urls')),

    # 视频管理
    path('video/',include('Videos.urls')),
    
    # 用户个人信息
    path('',include('Userprofile.urls')),

    # 评论管理
    path('comment/',include('comment.urls')),

    # 帖子管理
    path('article/',include('article.urls')),

    # 通知信息
    path('inbox/notifications/',include(notifications.urls,namespace='notifications')),

    path('notice/',include('notice.urls',namespace='notice')),

    # 小组信息
    path('group/',include('Usergroup.urls',namespace='group')),

    # 举报
    path('report/',include('report.urls',namespace='report')),

    # 申请
    path('ask/',include('askManage.urls',namespace='ask')),

    # 话题
    path('topic/',include('topic.urls',namespace='topic')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
