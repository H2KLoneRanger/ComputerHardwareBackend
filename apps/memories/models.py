from django.db import models


# 内存信息表模型类
class Memory(models.Model):
    # 内存信息表字段
    name = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="内存名称")
    price = models.FloatField(null=True, blank=True, verbose_name="内存价格")
    manufacturer = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="制造厂方")
    applicable_type = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="适用类型")
    memory_type = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="内存类型")
    memory_dominant_frequency = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="内存主频")
    total_memory_capacity = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="内存总容量")
    memory_capacity_description = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="内存容量描述")
    features = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="内存特点")
    number_of_pins = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="插脚数目")
    working_sequence = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="工作时序")
    memory_voltage = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="内存电压")

    class Meta:
        verbose_name = "内存信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
