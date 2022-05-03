from django.db import models


# 显卡信息表的模型类
class GPU(models.Model):
    # 显卡信息表字段
    name = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="显卡名称")
    price = models.FloatField(null=True, blank=True, verbose_name="显卡价格")
    manufacturer = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="制造厂方")
    GPU_type = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="显卡类型")
    chip_model = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="芯片型号")
    chip_code = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="芯片代号")
    manufacturing_process = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="制造工艺")
    GPU_interface_standard = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="显卡接口标准")
    output_interface = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="输出接口")
    multi_screen_display = models.IntegerField(null=True, blank=True, verbose_name="多屏显示")
    video_memory_capacity = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="显存容量")
    video_memory_type = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="显存类型")
    video_memory_width = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="显存位宽")
    core_frequency = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="核心频率")
    video_memory_frequency = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="显存频率")
    stream_processor_unit = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="流处理器单元")
    DirectX_version = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="DirectX 版本")
    maximum_resolution = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="最大分辨率")
    heat_dissipation_description = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="散热描述")
    power_interface = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="电源接口")
    board_size = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="板卡尺寸")
    characteristic_function = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="特色功能")
    TDP = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="热功耗设计")

    class Meta:
        verbose_name = "显卡信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
