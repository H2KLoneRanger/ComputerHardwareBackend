from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from powers.models import Power
from powers.serializers import PowersDetailSerializer


# 电源详情页的视图
class PowersDetailView(ListAPIView):
    queryset = Power.objects.all()
    serializer_class = PowersDetailSerializer

    # 重写ListAPIView里的list方法
    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        powers = self.get_queryset().filter(id=pk).first()

        serializer = self.get_serializer(powers)

        response = serializer.data
        return Response(response)
