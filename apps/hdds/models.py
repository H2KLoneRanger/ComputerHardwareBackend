from django.db import models


# 机械硬盘信息表模型类
class HDD(models.Model):
    # 机械硬盘信息表字段
    name = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="机械硬盘名称")
    price = models.FloatField(null=True, blank=True, verbose_name="机械硬盘价格")
    manufacturer = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="制造厂方")
    transmission_standard = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="传输标准")
    disk_type = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="机械硬盘类型")
    capacity = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="机械硬盘容量")
    rotational_speed = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="转速")
    cache_capacity = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="缓存容量")
    disk_size = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="盘体尺寸")
    interface_type = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="接口类型")

    class Meta:
        verbose_name = "机械硬盘信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
