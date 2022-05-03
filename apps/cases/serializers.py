from rest_framework import serializers

from cases.models import Case


# CPU信息序列化器
class CasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"


# CPU详细信息序列化器
class CasesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'
