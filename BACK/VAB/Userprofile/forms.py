from django import forms
from django.contrib.auth.models import User
import re  # 正则模块


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.'?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)


# 注册表类
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=255)
    email = forms.EmailField(label='Email')
    password_1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    # 清洗验证用户名
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("用户名必须大于三个字段")
        elif len(username) > 50:
            raise forms.ValidationError("用户名必须小于50个字段")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("该用户名已存在")

        return username

    # 清洗验证邮箱
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email_check(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError("该邮箱已经存在")
        else:
            raise forms.ValidationError("请输入有效邮件地址")

        return email

    # 清洗验证密码
    def clean_password_1(self):
        password_1 = self.cleaned_data.get('password_1')
        if len(password_1) < 3:
            raise forms.ValidationError("密码太短")
        elif len(password_1) > 20:
            raise forms.ValidationError("密码太长")

        return password_1

    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')

        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError('两次密码输入不同')

        return password_2


# 登录类
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    # 清洗验证用户名
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if email_check(username):
            filter_result = User.objects.filter(email__exact=username)
            if not filter_result:
                raise forms.ValidationError('该邮箱不存在')
        else:
            filter_result = User.objects.filter(username__exact=username)
            if not filter_result:
                raise forms.ValidationError('该用户名不存在，请先注册')

        return username


# 用户信息
class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, required=False)
    last_name = forms.CharField(label='Last Name', max_length=50, required=False)
    org = forms.CharField(label='Organization', max_length=50, required=False)
    telephone = forms.CharField(label='Telephone', max_length=50, required=False)
    personal_infor = forms.CharField(label='Personal_intro',required=False)


# 修改密码
class PwdChangeForm(forms.Form):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput)
    password_1 = forms.CharField(label='New Password', widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    def clean_password_1(self):
        password_1 = self.cleaned_data.get('password_1')

        if len(password_1) < 6:
            raise forms.ValidationError("密码太短了")
        elif len(password_1) > 20:
            raise forms.ValidationError("密码太长了")

        return password_1

    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')

        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError("两次密码不匹配，请重新输入")

        return password_2
