from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from hdds.models import HDD
from hdds.serializers import HDDsDetailSerializer


# 机械硬盘详情页的视图
class HDDsDetailView(ListAPIView):
    queryset = HDD.objects.all()
    serializer_class = HDDsDetailSerializer

    # 重写ListAPIView里的list方法
    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        hdds = self.get_queryset().filter(id=pk).first()

        serializer = self.get_serializer(hdds)

        response = serializer.data
        return Response(response)
