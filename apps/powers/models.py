from django.db import models


# 电源信息表模型类
class Power(models.Model):
    # 电源信息表字段
    name = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="电源名称")
    price = models.FloatField(null=True, blank=True, verbose_name="电源价格")
    manufacturer = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="制造厂方")
    power_standard = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="电源标准")
    rated_power = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="额定功率")
    max_power = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="最大功率")
    fan_description = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="风扇描述")
    certification_specification = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="认证规范")
    mainboard_interface = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="主板电源接口")
    CPU_interface = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="CPU供电接口")
    large4pin_interface = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="供电接口(大4pin)")
    SATA_interface = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="SATA接口")
    GPU_interface_8pin = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="8Pin显卡电源接口")
    AC_input = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="交流输入")
    PFC_type = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="PFC类型")
    plus80_certification = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="80PLUS认证")
    conversion_efficiency = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="转换效率")
    power_size = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="电源尺寸")

    class Meta:
        verbose_name = "电源信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
