from django.urls import re_path


from ssds import views

urlpatterns = [
    # 参数详情页的路由
    re_path(r'^ssds/(?P<pk>.*)/$', views.SSDsDetailView.as_view()),
]