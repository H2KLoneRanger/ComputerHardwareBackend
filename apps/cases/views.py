from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from cases.models import Case
from cases.serializers import CasesDetailSerializer


# CPU详情页的视图
class CasesDetailView(ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CasesDetailSerializer

    # 重写ListAPIView里的list方法
    def list(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        cases = self.get_queryset().filter(id=pk).first()

        serializer = self.get_serializer(cases)

        response = serializer.data
        return Response(response)
