from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from cpus.models import CPU
from cpus.serializers import CPUsDetailSerializer, CPUsSerializer


# 自定义分页类
class CPUPagination(PageNumberPagination):
    page_size = 10  # 一页显示10条数据
    page_size_query_param = 'page_size'  # 分页的参数值
    page_query_param = 'pageNo'  # 指定分多少页的参数
    max_page_size = 100  # 指定最多分多少页


# CPU所有数据的视图
class CPUsListView(ListAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUsSerializer
    pagination_class = CPUPagination  # 调用自定义的分页类


# CPU详情页的视图
class CPUsDetailView(ListAPIView):
    queryset = CPU.objects.all()
    serializer_class = CPUsDetailSerializer

    # 重写ListAPIView里的list方法
    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        cpus = self.get_queryset().filter(id=pk).first()

        serializer = self.get_serializer(cpus)

        response = serializer.data
        return Response(response)
