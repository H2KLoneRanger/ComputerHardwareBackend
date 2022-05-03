from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from mainboards.models import Mainboard
from mainboards.serializers import MainboardsDetailSerializer


# 主板详情页视图
class MainboardsDetailView(ListAPIView):
    queryset = Mainboard.objects.all()
    serializer_class = MainboardsDetailSerializer

    # 重写ListAPIView里的list方法
    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        mainboards = self.get_queryset().filter(id=pk).first()

        serializer = self.get_serializer(mainboards)

        response = serializer.data
        return Response(response)
    