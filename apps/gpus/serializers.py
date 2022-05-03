from rest_framework import serializers

from gpus.models import GPU


# 显卡信息序列化器
class GPUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = "__all__"


# 显卡详细信息序列化器
class GPUsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = '__all__'
