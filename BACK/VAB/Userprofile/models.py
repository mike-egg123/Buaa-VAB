from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # CASCADE级联删除
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    org = models.CharField('Organization', max_length=255, blank=True)
    telephone = models.CharField('Telephone', max_length=50, blank=True)
    mod_date = models.DateTimeField('last modified', auto_now=True)
    headshot = models.ImageField(upload_to='headshot', null=True)
    personal_infor = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'User profile'

    def __str__(self):
        return "{}".format(self.user.__str__)


'''
User模型自带属性：
    username：用户名
    email: 电子邮件
    password：密码
    first_name：名
    last_name：姓
    is_active: 是否为活跃用户。默认是True
    is_staff: 是否为员工。默认是False
    is_superuser: 是否为管理员。默认是False
    date_joined: 加入日期。系统自动生成
'''
