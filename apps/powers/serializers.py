from rest_framework import serializers

from powers.models import Power


# 电源信息序列化器
class PowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = "__all__"


# 电源详细信息序列化器
class PowersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = '__all__'
