# Generated by Django 3.2.10 on 2022-04-26 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpu',
            name='DirectX_version',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='DirectX 版本'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='GPU_interface_standard',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='显卡接口标准'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='GPU_type',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='显卡类型'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='board_size',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='板卡尺寸'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='characteristic_function',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='特色功能'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='chip_code',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='芯片代号'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='chip_model',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='芯片型号'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='heat_dissipation_description',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='散热描述'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='manufacturer',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='制造厂方'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='manufacturing_process',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='制造工艺'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='maximum_resolution',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='最大分辨率'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='name',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='显卡名称'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='output_interface',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='输出接口'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='power_interface',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='电源接口'),
        ),
        migrations.AlterField(
            model_name='gpu',
            name='video_memory_type',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='显存类型'),
        ),
    ]