from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from gpus.models import GPU
from gpus.serializers import GPUsDetailSerializer


# 显卡详情页的视图
class GPUsDetailView(ListAPIView):
    queryset = GPU.objects.all()
    serializer_class = GPUsDetailSerializer

    # 重写ListAPIView里的list方法
    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        gpus = self.get_queryset().filter(id=pk).first()

        serializer = self.get_serializer(gpus)

        response = serializer.data
        return Response(response)
