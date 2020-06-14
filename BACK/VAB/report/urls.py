from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('report-Bookcomment/<int:id>/',views.RBookComment,name='report_Bookcomment'),
    path('report-Videocomment/<int:id>/',views.RVideoComment,name='report_Videocomment'),
    path('report-Articlecomment/<int:id>/',views.RArticleComment,name='report_Articlecomment'),
    path('allMyreport',views.LookAllMyReport,name='allMyreport'),
    path('needhandle',views.needhandleReport,name='needHandle'),
    path('refuse-bookreport/<int:id>/',views.refusebookreport,name='refuseBR'),
    path('refuse-videoreport/<int:id>/',views.refusevideoreport,name='refuseVR'),
    path('refuse-articlereport/<int:id>/',views.refusearticlereport,name='refuseAR'),
    path('handle-bookreport/<int:id>/',views.handlebookreport,name='handleBR'),
    path('handle-videoreport/<int:id>/',views.handlevideoreport,name='handleVR'),
    path('handle-articlereport/<int:id>/',views.handlearticlereport,name='handleAR'),
]