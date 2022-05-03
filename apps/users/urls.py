# users子路由
from rest_framework_jwt.views import obtain_jwt_token

from users import views
from django.urls import path

urlpatterns = [
    # 短信验证码路由
    path('code/', views.VerifyCodeView.as_view()),
    # 用户注册的路由地址
    path('users/', views.RegisterView.as_view()),
    # 用户登录的路由地址
    path('login/', obtain_jwt_token),
]