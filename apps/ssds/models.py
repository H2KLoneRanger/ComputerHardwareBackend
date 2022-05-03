from django.db import models


# 固态硬盘信息表模型类
class SSD(models.Model):
    # 固态硬盘信息表字段
    name = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="固态硬盘名称")
    price = models.FloatField(null=True, blank=True, verbose_name="固态硬盘价格")
    manufacturer = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="制造厂方")
    capacity = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="固态硬盘容量")
    cache_capacity = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="缓存容量")
    flash_type = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="闪存类型")
    max_continuous_read_speed = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="连续读取最大速度")
    max_continuous_write_speed = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="连续写入最大速度")
    disk_size = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="硬盘尺寸")
    interface_type = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="接口类型")

    class Meta:
        verbose_name = "固态硬盘信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
