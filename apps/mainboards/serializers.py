from rest_framework import serializers
from mainboards.models import Mainboard


# 主板信息序列化器
class MainboardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainboard
        fields = "__all__"


# 主板详细信息序列化器
class MainboardsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainboard
        fields = '__all__'
