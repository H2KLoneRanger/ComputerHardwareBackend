from django.urls import re_path, path
from rest_framework.routers import DefaultRouter

from cpus import views

urlpatterns = [
    # CPU所有数据的路由
    path('cpus/', views.CPUsListView.as_view()),
    # CPU参数详情页的路由
    re_path(r'^cpus/(?P<pk>.*)/$', views.CPUsDetailView.as_view()),
]

# DRF的路由方式
# router = DefaultRouter()
# router.register(r'cpus', views.CPUsListView.as_view(), basename='cpus')
# urlpatterns += router.urls


