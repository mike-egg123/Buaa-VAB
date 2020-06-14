from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import RegistrationForm, LoginForm, ProfileForm, PwdChangeForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib import auth,messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from article.models import Article
from Books.models import Book
from Videos.models import Video

# VAB主站点
def loadHomepage(request):
    articles = []
    books = []
    videos = []

    acount = 3
    bcount = 3
    vcount = 3

    if Article.objects.all().count() < 3:acount = Article.objects.all().count()
    if Book.objects.all().count() < 3:bcount = Book.objects.all().count()
    if Video.objects.all().count() < 3:vcount = Video.objects.all().count()

    alist = Article.objects.all().order_by('-total_views')
    blist = Book.objects.all().order_by('-Book_total_views')
    vlist = Video.objects.all()

    for i in range(0,acount):articles.append(alist[i])
    for j in range(0,bcount):books.append(blist[j])
    for k in range(0,vcount):videos.append(vlist[k])

    context = {'articles':articles,'books':books,'videos':videos}

    return render(request, 'homepage.html',context)

# 个人信息
@login_required
def profile(request, id):
    user = User.objects.get(id=id)
    userprofile = UserProfile.objects.get(user_id=id)
    return render(request, 'Userprofile/profile.html', {'user': user,'userprofile':userprofile})


# 更新个人信息
@login_required
def profile_update(request, id):
    user = get_object_or_404(User, pk=id)
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        if request.user != user:
            return HttpResponse("你没有权限修改该用户的个人信息")

        form = ProfileForm(request.POST,request.FILES)

        if form.is_valid():
            # 从表单中洗出数
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            user_profile.telephone = form.cleaned_data['telephone']
            user_profile.personal_infor = form.cleaned_data['personal_infor']
            # user_profile.birthday = form.cleaned_data['date1']

            if 'file_profile' in request.FILES:
                user_profile.headshot = request.FILES.get('file_profile')

            user_profile.save()
            return redirect("Userprofile:profile",id=user.id)
        else:
            return HttpResponse("个人信息更新错误，请重试")

    else:
        default_data = {'user':user,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'org': user_profile.org,
                        'userprofile':user_profile,
                        'telephone': user_profile.telephone,
                        'personal_intro':user_profile.personal_infor,
                        'headshot':user_profile.headshot,
                        'email':user.email,}
        form = ProfileForm()

    return render(request, 'Userprofile/profile_update.html', default_data)


# 注册
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            orgin_pwd = form.cleaned_data['password_1']
            password = form.cleaned_data['password_2']

            # 使用内置create
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email)
            userprofile = UserProfile.objects.create(user=user)
            login(request,user)
            return redirect('showBook')
        else:
            return HttpResponse("<script>alert('填写错误，请重试');location.href=\"\";</script>")

    else:
        form = RegistrationForm()
        return render(request, 'Userprofile/registration.html', {'form': form})


# 登录
def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            print(username)
            print(password)

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                print(user.id)
                # return redirect('Userprofile:profile', id=user.id)
                return redirect('showBook')
            else:
                return render(request, 'Userprofile/login.html', {'form': form,
                                                                  'message': '用户名或密码错误，请再输一次'})

    else:
        form = LoginForm()

    return render(request, 'Userprofile/login.html', {'form': form})


# 登出
@login_required
def userlogout(request):
    logout(request)
    return redirect('Userprofile:loadHomepage')


# 修改密码
@login_required
def pwd_change(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = PwdChangeForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data['old_password']
            username = user.username

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                new_password = form.cleaned_data['password_2']
                user.set_password(new_password)
                user.save()
                return HttpResponseRedirect('/accounts/login/')
            else:
                return render(request, 'Userprofile/pwd_change.html',
                              {'form': form, 'user': user, 'message': '您的旧密码不对，请重新输入'})

    else:
        form = PwdChangeForm()

    return render(request, 'Userprofile/pwd_change.html', {'form': form, 'user': user})

# 处理ajax请求
def registerajax(request):
    result = {"code":1000,"msg":""}

    if request.method == "POST":
        username = request.POST.get("username")
        password_1 = request.POST.get("password_1")
        password_2 = request.POST.get("password_2")
        email = request.POST.get("email")

        if username and password_1 and password_2:
            user = User.objects.filter(username__exact=username).first()
            emailueser = User.objects.filter(email__exact=email).first()
            if user:
                result = {"code":1001,"msg":"用户名已被使用"}
            else:
                if emailueser:
                    result = {"code": 1002, "msg": "邮箱已被使用"}
                else:
                    if password_1 != password_2:
                        result = {"code": 1003, "msg": "两次输入的密码不一样"}
                    else:
                        newuser = User.objects.create_user(username=username,
                                                        password=password_2,
                                                        email=email)
                        userprofile = UserProfile.objects.create(user=newuser)
                        result = {"code":1004,"msg":"注册成功"}
        else:
            result = {"code": 1005, "msg": "用户名或者密码为空"}
    return JsonResponse(result)


# 判断用户是否存在
def checkusers(request):
    result = {"code":2000,"msg":""}
    username = request.GET.get("username")
    if username:
        user = User.objects.filter(username__exact=username).first()
        if user:
            result = {"code":2000,"msg":"用户名存在"}
        else:
            result = {"code": 2001, "msg": ""}
    else:
        result = {"code": 2002, "msg": "请输入用户名"}
    return JsonResponse(result)

# 判断用户是否存在
def checkusers_login(request):
    result = {"code":2000,"msg":""}
    username = request.GET.get("username")
    if username:
        user = User.objects.filter(username__exact=username).first()
        if user:
            result = {"code":2000,"msg":""}
        else:
            result = {"code": 2001, "msg": "用户名不存在"}
    else:
        result = {"code": 2002, "msg": "请输入用户名"}
    return JsonResponse(result)


# 判断邮箱是否已经被使用
def checkemail(request):
    result = {"code":3000,"msg":""}
    email = request.GET.get("email")
    if email:
        user = User.objects.filter(email__exact=email).first()
        if user:
            result = {"code":3000,"msg":"邮箱已被使用"}
        else:
            result = {"code": 3001, "msg": ""}
    else:
        result = {"code": 3002, "msg": "请输入邮箱"}
    return JsonResponse(result)

# 密码是否重复
def checkpwd(request):
    result = {"code": 4000, "msg": ""}

    pwd_1 = request.GET.get("password_1")
    pwd_2 = request.GET.get("password_2")


    if pwd_1 and pwd_2:
        if pwd_1 != pwd_2:
            result = {"code": 4000, "msg": "密码不一致"}
        else:
            result = {"code": 4001, "msg": ""}
    else:
        result = {"code": 4002, "msg": "请输入密码"}
    return JsonResponse(result)

def checkpwd_login(request):
    result = {"code": 4000, "msg": ""}
    username = request.GET.get("username")
    password = request.GET.get("password")

    print(username)
    print(password)

    if username and password:
        user = User.objects.filter(username__exact=username,password=password).first()
        if user:
            result = {"code": 4000, "msg": ""}
        else:
            result = {"code": 4001, "msg": ""}
    else:
        result = {"code": 4002, "msg": "请输入用户名和密码"}
    return JsonResponse(result)

















