from django.urls import re_path


from mainboards import views

urlpatterns = [
    # 主板参数详情页的路由
    re_path(r'^mainboards/(?P<pk>.*)/$', views.MainboardsDetailView.as_view()),
]