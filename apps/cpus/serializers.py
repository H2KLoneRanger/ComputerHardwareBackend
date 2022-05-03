from rest_framework import serializers

from cpus.models import CPU


# CPU信息序列化器
class CPUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = "__all__"


# CPU详细信息序列化器
class CPUsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'
