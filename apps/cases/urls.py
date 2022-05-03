from django.urls import re_path


from cases import views

urlpatterns = [
    # 参数详情页的路由
    re_path(r'^cases/(?P<pk>.*)/$', views.CasesDetailView.as_view()),
]