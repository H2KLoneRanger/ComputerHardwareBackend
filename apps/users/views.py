import random
from rest_framework import status
from rest_framework_jwt.settings import api_settings  # 包不要倒入错了
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import VerifyCode, UserToken
from django_redis import get_redis_connection
from users.serializers import VerifyCodeSerializer, UserRegisterSerializer, LoginSerializer


# 短信验证码的视图
class VerifyCodeView(APIView):
    # 生成随机的四位数验证码
    def get_verify_code(self):
        number = '0123456789'
        random_code = ""
        for i in range(4):
            random_code += random.choice(number)  # 生成4位数的随机验证码
        return random_code

    # 验证码校验视图
    def post(self, request, *args, **kwargs):
        # 获取手机号和验证码
        data = request.data
        mobile = data.get('mobile')
        code = self.get_verify_code()

        # 校验手机号格式
        serializer = VerifyCodeSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        # 使用云通讯发送短信, 发送成功返回0，发送失败返回-1
        # result = CCP().send_template_sms(mobile, [code, 5], 1)
        result = 0 # 云通讯下节课再讲，这里默认发送成功

        # 判定短信验证码是否发送成功
        if result != 0:
            return Response({"mobile": "验证码发送失败"},status=status.HTTP_400_BAD_REQUEST)
        else:
            VerifyCode.objects.create(mobile=mobile, code=code)  # 创建一个验证码对象
            redis_conn = get_redis_connection('VerifyCode')  # 实例化一个redis连接对象
            redis_pipeline = redis_conn.pipeline()  # 实例化一个redis的管道对象
            redis_pipeline.setex('sms_%s' % mobile, 300, code)  # 通过管道设置redis中的键值对数据
            redis_pipeline.execute()  # 通过管道提交到redis中进行保存
            return Response({"mobile": "验证码发送成功"}, status=status.HTTP_201_CREATED)


# 用户注册视图
class RegisterView(APIView):

    # 注册用户
    def post(self, request):
        # 用户信息反序列化验证
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        # 创建用户的时候获取用户对象
        user = serializer.save()

        # 生成JWT信息
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        # 创建token信息保存在数据库中【新增】
        UserToken.objects.create(user=user, token=token)
        # 返回给前端
        dic = serializer.validated_data
        dic['token'] = token  # 往dic字典中添加token键值对
        headers = {'Authorization': 'Bearer %s' % token}

        return Response(dic, status=201, headers=headers)
        # return Response({'message': '注册成功'}, status=status.HTTP_201_CREATED)

    # users 接口的get请求方法，用于前端获取用户注册后的信息【新增】
    def get(self, request):
        # 用户对象，来自请求，通过验证方法之后所返回的用户对象，没有通过认证的用户为匿名用户
        user = request.user

        serializer = LoginSerializer(user)
        data = serializer.data
        data['mobile'] = user.username
        return Response(data)


