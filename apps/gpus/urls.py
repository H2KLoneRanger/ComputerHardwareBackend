from django.urls import re_path


from gpus import views

urlpatterns = [
    # 显卡参数详情页的路由
    re_path(r'^gpus/(?P<pk>.*)/$', views.GPUsDetailView.as_view()),
]