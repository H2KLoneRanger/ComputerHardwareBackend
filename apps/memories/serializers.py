from rest_framework import serializers

from memories.models import Memory


# 内存信息序列化器
class MemoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = "__all__"


# 内存详细信息序列化器
class MemoriesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = "__all__"
