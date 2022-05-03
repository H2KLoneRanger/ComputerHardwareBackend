from django.db import models


# CPU信息表的模型类
class CPU(models.Model):

    # CPU信息表字段
    name = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="CPU名称")
    price = models.FloatField(null=True, blank=True, verbose_name="CPU价格")
    manufacturer = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="制造厂方")
    series = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="系列")
    code_name = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="核心代号")
    total_cores = models.IntegerField(null=True, blank=True, verbose_name="内核数")
    total_threads = models.IntegerField(null=True, blank=True, verbose_name="线程数")
    sockets_supported = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="插槽类型")
    use_conditions = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="使用类型")
    architecture = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="架构")
    process_technology = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="制程工艺")
    base_frequency = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="核心频率")
    max_turbo_frequency = models.IntegerField(null=True, blank=True, verbose_name="最大睿频频率")
    cache = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="缓存")
    compatible_mainboard = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="兼容主板")
    launch_date = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="发行日期")
    is_64bit = models.BooleanField(default=1, null=True, blank=True, verbose_name="是否64位处理器")
    processor_graphics = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="处理器显卡")
    memory_channels = models.IntegerField(default=2, null=True, blank=True, verbose_name="最大内存通道数")
    memory_types = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="支持内存类型")
    TDP = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="热功耗设计")

    class Meta:
        verbose_name = "CPU信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
