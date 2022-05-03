from django.db import models


# 主板信息表的模型类
class Mainboard(models.Model):
    # 主板信息表字段
    name = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="主板名称")
    price = models.FloatField(null=True, blank=True, verbose_name="主板价格")
    manufacturer = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="制造厂方")
    chipset = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="芯片组")
    CPU_slot = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="CPU插槽")
    support_CPU_type = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="支持CPU类型")
    mainboard_architecture = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="主板架构")
    supported_memory_types = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="支持内存类型")
    memory_slot = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="内存插槽")
    memory_frequency = models.TextField(default="", null=True, blank=True, verbose_name="内存频率")
    max_memory_capacity = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="最大支持内存容量")
    onboard_sound_card = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="板载声卡")
    onboard_network_card = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="板载网卡")
    hard_disk_interface = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="硬盘接口")
    SATA_3_interface_number = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="SATA3接口数量")
    socket_interface = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="插槽接口")
    extension_interface = models.TextField(default="", null=True, blank=True, verbose_name="扩展接口")
    power_interface = models.CharField(max_length=254, default="", null=True, blank=True, verbose_name="电源接口")
    overall_dimension = models.CharField(max_length=64, default="", null=True, blank=True, verbose_name="外形尺寸")

    class Meta:
        verbose_name = "主板信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
