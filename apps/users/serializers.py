import re
import datetime

from django.contrib.auth import get_user_model
from django_redis import get_redis_connection
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import VerifyCode, UserInfo


# 短信验证码的序列化器
class VerifyCodeSerializer(serializers.Serializer):
    # 手机号字段
    mobile = serializers.CharField(max_length=11)

    # 校验短信验证码模型类的数据
    def validated_mobile(self, mobile):

        # 手机号是否已注册
        if UserInfo.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号格式是否正确
        if not re.match(r'^1[3-9]\d{9}', mobile):
            raise serializers.ValidationError("手机号码格式错误")

        # 短信验证码的发送频率
        one_minutes_ago = datetime.datetime.now() - datetime.timedelta(hours=0, minutes=1, seconds=0)

        # 验证短信一分钟内是否重复发送
        if VerifyCode.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送时间未超过60秒")

        return mobile


# 获取用户的模型，认证的模型对象
User = get_user_model()


# 用户注册的序列化器
class UserRegisterSerializer(serializers.Serializer):
    # 字段信息
    username = serializers.CharField(label='用户名', required=True,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已存在")])
    password = serializers.CharField(label='密码', style={'input_type': 'password'}, write_only=True)
    code = serializers.CharField(label='验证码', required=True, write_only=True,
                                 max_length=4, min_length=4, error_messages={
            'blank': '请输入验证码',
            'required': '请输入验证码',
            'max_length': '验证码格式错误',
            'min_length': '验证码格式错误',
        })

    # 信息校验
    def validate(self, attrs):
        # 获取手机号(前端手机号绑死了username字段)和验证码
        mobile = attrs.get('username')
        redis_conn = get_redis_connection('verify_codes')  # 先连接到redis
        code = redis_conn.get('sms_%s' % mobile).decode()  # 从redis中取出验证码

        # 验证码的格式验证
        if len(attrs.get('code')) != 4:
            raise serializers.ValidationError('验证码格式错误')
        # 验证码是否有效
        if not code:
            raise serializers.ValidationError('验证码已过期')
        # 验证码是否正确
        if attrs.get('code') != code:
            raise serializers.ValidationError('验证码错误')
        # 验证密码的长度
        if len(attrs.get('password')) < 6 or len(attrs.get('password')) > 20:
            raise serializers.ValidationError('密码长度不正确，应该为6-20位')
        # 验证密码的组成格式
        if not attrs.get('password').isalnum():
            raise serializers.ValidationError('密码应该由字母和数字组成')
        # 验证密码
        if not re.match(r'[a-zA-Z]{1,19}\d+', attrs.get('password')):
            raise serializers.ValidationError('密码不正确')

        return attrs

    # 创建用户对象
    def create(self, validated_data):
        del validated_data['code']  # 删除验证码信息
        # user = User.objects.create(**validated_data) # 创建用户
        user = User(**validated_data)  # 创建用户并获取用户对象
        user.set_password(user.password)  # 将用户的明文密码进行加密
        user.save()  # 保存修改后的密码信息
        return user

    class Meta:
        model = User
        fields = '__all__'


# 增加登录的序列化器
class LoginSerializer(serializers.ModelSerializer):
    # 字段信息
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False)
    password = serializers.CharField(label="密码", style={'input_type': 'password'}, write_only=True)

    # 校验数据
    def validate(self, attrs):
        mobile = attrs.get('username')  # 获取手机号
        # 判断手机号
        if not re.match(r'^1[3-9]\d{9}', attrs.get('username')):
            raise serializers.ValidationError('用户名不合法，请重新输入')
        # 判断密码长度
        if len(attrs.get('password')) < 6 or len(attrs.get('password')) > 20:
            raise serializers.ValidationError('密码长度不正确，应为6-20位')
        # 判断密码组成
        if not attrs.get('password').isalnum():
            raise serializers.ValidationError('密码应由字母与数字组成')
        # 验证密码
        if not re.match(r'[a-zA-Z]{1,19}\d+', attrs.get('password')):
            raise serializers.ValidationError('密码不正确')
        return attrs

    class Meta:
        model = User
        fields = '__all__'
