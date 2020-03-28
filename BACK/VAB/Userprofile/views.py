from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import RegistrationForm, LoginForm, ProfileForm, PwdChangeForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# 个人信息
@login_required
def profile(request, id):
    user = get_object_or_404(User, id=id)
    userprofile = get_object_or_404(UserProfile, id=id)
    return render(request, 'Userprofile/profile.html', {'user': user,'userprofile':userprofile})


# 更新个人信息
@login_required
def profile_update(request, id):
    user = get_object_or_404(User, pk=id)
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)

        if form.is_valid():
            # 从表单中洗出数
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            user_profile.org = form.cleaned_data['org']
            user_profile.telephone = form.cleaned_data['telephone']
            user_profile.personal_infor = form.cleaned_data['personal_infor']
            user_profile.headshot = request.FILES.get('headshot')
            user_profile.save()

            # reverse反转urls并传递参数
            return HttpResponseRedirect(reverse('Userprofile:profile', args=[user.id]))

    else:
        default_data = {'first_name': user.first_name,
                        'last_name': user.last_name,
                        'org': user_profile.org,
                        'telephone': user_profile.telephone,
                        'personal_intro':user_profile.personal_infor,
                        'headshot':user_profile.headshot}
        form = ProfileForm(default_data)

    return render(request, 'Userprofile/profile_update.html', {'form': form, 'user': user})


# 注册
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password_2']

            # 使用内置create
            user = User.objects.create_user(username=username,
                                            password=password,
                                            email=email)
            userprofile = UserProfile.objects.create(user=user)
            login(request,user)
            return redirect('Userprofile:profile', id=user.id)
        else:
            return HttpResponse("填写错误，请重试")
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

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                print(user.id)
                return redirect('Userprofile:profile', id=user.id)
            else:
                return render(request, 'Userprofile/login.html', {'form': form,
                                                                  'message': '密码错误，请再输一次'})

    else:
        form = LoginForm()

    return render(request, 'Userprofile/login.html', {'form': form})


# 登出
@login_required
def userlogout(request):
    auth.logout(request, pk)
    return HttpResponseRedirect("/accounts/login/")


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








