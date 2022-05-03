from django.contrib.auth.models import AbstractUser
from django.db import models


# 继承Django自带的认证模型类，然后补充字段信息
class UserInfo(AbstractUser):
    # 性别字段可选参数
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )

    # 用户信息字段
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="male", verbose_name="性别")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 短信验证码的模型类
class VerifyCode(models.Model):
    # 字段信息
    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    add_time = models.DateTimeField(auto_now=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name
        ordering = ['-add_time']

    def __str__(self):
        return self.code


# 创建token模型类，用于保存token信息
class UserToken(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE, verbose_name='用户')
    token = models.CharField(max_length=255, verbose_name='用户令牌')

    class Meta:
        db_table = 'UserToken'
