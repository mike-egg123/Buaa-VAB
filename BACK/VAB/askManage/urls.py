from django.urls import path
from . import views

app_name = 'ask'

urlpatterns = [
    path('ask-Formanage/<int:id>/',views.makeAsk,name='makeAsk'),
    path('allMyasks/<int:id>/',views.allMyask,name='allMyasks'),
    path('need-handle-asks/<int:id>/',views.handleAsk,name='NeedHandleAsks'),
]