from rest_framework import serializers

from ssds.models import SSD


# 固态硬盘信息序列化器
class SSDsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSD
        fields = "__all__"


# SSD详细信息序列化器
class SSDsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSD
        fields = '__all__'
