from django.db import models


# 机箱信息表模型类
class Case(models.Model):
    # 机箱信息表字段
    name = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="机箱名称")
    price = models.FloatField(null=True, blank=True, verbose_name="机箱价格")
    manufacturer = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="制造厂方")
    applicable_type = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="适用类型")
    case_style = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="机箱样式")
    case_type = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="机箱类型")
    compatible_mainboard = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="兼容主板")
    case_bin = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="机箱仓位")
    expansion_slots = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="扩展插槽")
    case_material = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="机箱材质")
    case_color = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="机箱颜色")
    case_weight = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="机箱重量")
    front_interface_description = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="前置接口描述")
    case_fan = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="机箱风扇")
    internal_heat_dissipation_description = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="内部散热描述")
    support_water_cooling = models.BooleanField(default=False, null=True, blank=True, verbose_name="支持水冷")
    GPU_length_limit = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="显卡限长")
    radiator_height_limit = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="散热器限高")
    power_location = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="电源位置")
    support_back_routing = models.BooleanField(default=False, null=True, blank=True, verbose_name="支持背部走线")
    case_size = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="机箱尺寸")
    other_properties = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="其它性能")

    class Meta:
        verbose_name = "机箱信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
