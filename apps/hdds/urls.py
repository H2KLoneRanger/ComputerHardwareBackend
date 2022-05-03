from django.urls import re_path


from hdds import views

urlpatterns = [
    # 机械硬盘参数详情页的路由
    re_path(r'^hdds/(?P<pk>.*)/$', views.HDDsDetailView.as_view()),
]