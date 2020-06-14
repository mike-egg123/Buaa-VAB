from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.http import HttpResponseRedirect

# 方法装饰器
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User

from .models import Ask
from Usergroup.models import Usergroup

# 发起申请
def makeAsk(request,id):
    ask = Ask.objects.create(
        asker=request.user,
        group=Usergroup.objects.get(id=id),
    )
    return redirect("Usergroup:Groupdetail",id=id)

# 查看我的申请
def allMyask(request,id):
    user = User.objects.get(id=id)
    allmyasking = Ask.objects.filter(asker_id=id)
    context = {'allmyasking':allmyasking}
    print(allmyasking)
    return render(request,'askManage/allMyAsk.html',context)

# 查看我需要处理的申请
def handleAsk(request,id):
    user = User.objects.get(id=id)
    mygroups = Usergroup.objects.filter(groupMaster_id=user.id)
    allAsks = []
    for agroup in mygroups:
        asks = Ask.objects.filter(group_id=agroup.id)
        for aask in asks:
            allAsks.append(aask)
    context = {'asks':allAsks}
    return render(request,'askManage/needHandleAsk.html',context)