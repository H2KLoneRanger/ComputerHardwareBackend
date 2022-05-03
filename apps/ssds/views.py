from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from ssds.models import SSD
from ssds.serializers import SSDsDetailSerializer


# 固态硬盘详情页的视图
class SSDsDetailView(ListAPIView):
    queryset = SSD.objects.all()
    serializer_class = SSDsDetailSerializer

    # 重写ListAPIView里的list方法
    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        ssds = self.get_queryset().filter(id=pk).first()

        serializer = self.get_serializer(ssds)

        response = serializer.data
        return Response(response)
