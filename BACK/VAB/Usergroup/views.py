from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import GroupForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Q

from .models import Usergroup
from Userprofile.models import UserProfile
from article.models import Article
from askManage.models import Ask

# 小组列表（展示目前所有小组）
def showGroup(request):
    search = request.GET.get('search')

    allgroups = Usergroup.objects.all().order_by('-groupsize')

    if search:
        group_list = Usergroup.objects.all().order_by('-groupsize').filter(
            Q(groupname__icontains=search) |
            Q(group_info__icontains=search)
        )
    else:
        search = ''
        group_list = Usergroup.objects.all().order_by('-groupsize')

    paginator = Paginator(group_list, 4)
    page = request.GET.get('page')
    groups = paginator.get_page(page)

    if group_list.count() < 3:
        recommend_list = None
    else:
        recommend_list = [group_list[0], group_list[1],group_list[2]]

    context = {
        'groups':groups,
        'search': search ,
        'group_list':group_list,
        'groupcount':len(Usergroup.objects.all()),
        'recommend_list':recommend_list
    }

    return render(request, 'Usergroup/showGroups.html', context)


# 显示小组具体信息
def GroupDetail(request,id):
    # 小组的基本信息
    group = Usergroup.objects.get(id=id)
    members = group.members.all()
    master = group.groupMaster

    user_state = 0 # 默认游客状态
    is_member = group.members.filter(id=request.user.id).exists()
    is_manager = group.group_managers.filter(id=request.user.id).exists()
    is_master = (group.groupMaster.id == request.user.id)

    if is_member:
        user_state = 1 # 普通成员状态
        if is_manager:
            user_state = 2 # 管理员状态
            if is_master:
                user_state = 3 # 群主

    articles = []
    membersProfile = []
    # 找出小组成员的帖子
    for person in members:
        articles.extend(Article.objects.filter(author_id__exact=person.id))
        membersProfile.extend(UserProfile.objects.filter(user_id=person.id))


    context = {'group':group,'members':members,'master':master,'articles':articles,'profiles':membersProfile,'user_state':user_state}
    return render(request, 'Usergroup/GroupDetail.html',context)

# 创建小组
@method_decorator(login_required, name='post')
class GroupCreate(View):
    form_class = GroupForm
    initial = {}
    template_name = 'Usergroup/CreateGroup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            groupname = form.cleaned_data['groupname']
            master = User.objects.get(id=request.user.id)
            groupinfo = form.cleaned_data['group_info']
            groupimg = request.FILES.get('group_img')
            groupsize = 1
            group = Usergroup.objects.create(
                groupname=groupname,
                groupMaster=master,
                group_info=groupinfo,
                groupsize=groupsize,
                group_img=groupimg
            )
            group.members.add(master)
            group.group_managers.add(master)
            group.save()

            return redirect("Usergroup:Groupdetail",id=group.id)
        else:
            print("Group:error!")
        return render(request, self.template_name, {'form':form})


# 查询自己所在小组
def MyGroupList(request):
    user_me = User.objects.get(id=request.user.id)
    mygroups = user_me.members.all()

    context = {'mygroups':mygroups}
    return render(request, 'Usergroup/MyGroups.html', context)


# 加入小组
def JoinGroup(request,id):
    group = Usergroup.objects.get(id=id)

    memberset = group.members.all()

    if memberset.filter(id=request.user.id):
        return HttpResponse("您已经在小组中了")
    else:
        person = User.objects.get(id=request.user.id)
        group.groupsize += 1
        group.members.add(person)
        group.save()
        return redirect('group:Groupdetail',id=id)

# 同意成为管理员
def AgreeAsk(request,id):
    ask = Ask.objects.get(id=id)
    group = ask.group
    asker = ask.asker
    group.group_managers.add(asker)
    group.save()

    # 完成处理
    ask.state = 2
    ask.save()

    return redirect('ask:NeedHandleAsks',id=request.user.id)

# 拒绝成为管理员
def RefuseAsk(request,id):
    ask = Ask.objects.get(id=id)
    ask.state = 1
    ask.save()

    return redirect('ask:NeedHandleAsks',id=request.user.id)


# 退出小组
def ExitGroup(request,id):
    # 组长退群 -- 删除小组
    group = Usergroup.objects.get(id=id)
    master = group.groupMaster

    if master.id == request.user.id:
        Usergroup.objects.filter(id=id).delete()
        return redirect('group:showGroup')
    # 成员退群
    else:
        memberset = group.members.all()
        managers = group.group_managers.all()

        if managers.filter(id=request.user.id).exists():
            userme = User.objects.all().get(id=request.user.id)
            group.group_managers.remove(userme)
            group.groupsize -= 1
            group.members.remove(userme)
            group.save()
            return redirect('group:showGroup')

        if memberset.filter(id=request.user.id).exists():
            userme = User.objects.all().get(id=request.user.id)
            group.groupsize -= 1
            group.members.remove(userme)
            group.save()
            return redirect('group:showGroup')
        else:
            return HttpResponse("您还没有加入小组")

# 置顶帖子
def topArticle(request,id,article_id):
    article = Article.objects.get(id=article_id)
    group = Usergroup.objects.get(id=id)

    group.top_article = article
    group.save()

    return redirect('group:Groupdetail',group.id)

















