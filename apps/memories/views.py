from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from memories.models import Memory
from memories.serializers import MemoriesDetailSerializer


# 内存详情页的视图
class MemoriesDetailView(ListAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemoriesDetailSerializer

    # 重写ListAPIView里的list方法
    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        memories = self.get_queryset().filter(id=pk).first()

        serializer = self.get_serializer(memories)

        response = serializer.data
        return Response(response)
