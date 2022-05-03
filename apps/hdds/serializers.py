from rest_framework import serializers

from hdds.models import HDD


# 机械硬盘信息序列化器
class HDDsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HDD
        fields = "__all__"


# 机械硬盘详细信息序列化器
class HDDsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HDD
        fields = '__all__'
