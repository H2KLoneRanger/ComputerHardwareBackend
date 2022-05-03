from django.urls import re_path


from memories import views

urlpatterns = [
    # 内存参数详情页的路由
    re_path(r'^memories/(?P<pk>.*)/$', views.MemoriesDetailView.as_view()),
]