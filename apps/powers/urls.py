from django.urls import re_path


from powers import views

urlpatterns = [
    # 参数详情页的路由
    re_path(r'^powers/(?P<pk>.*)/$', views.PowersDetailView.as_view()),
]