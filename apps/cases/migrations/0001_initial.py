# Generated by Django 3.2.10 on 2022-04-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, verbose_name='机箱名称')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='机箱价格')),
                ('manufacturer', models.CharField(default='', max_length=128, verbose_name='制造厂方')),
                ('applicable_type', models.CharField(default='', max_length=64, verbose_name='适用类型')),
                ('case_style', models.CharField(default='', max_length=64, verbose_name='机箱样式')),
                ('case_type', models.CharField(default='', max_length=64, verbose_name='机箱类型')),
                ('compatible_mainboard', models.CharField(default='', max_length=128, verbose_name='兼容主板')),
                ('case_bin', models.CharField(default='', max_length=128, verbose_name='机箱仓位')),
                ('expansion_slots', models.CharField(default='', max_length=128, verbose_name='扩展插槽')),
                ('case_material', models.CharField(default='', max_length=64, verbose_name='机箱材质')),
                ('case_color', models.CharField(default='', max_length=64, verbose_name='机箱颜色')),
                ('case_weight', models.CharField(default='', max_length=64, verbose_name='机箱重量')),
                ('front_interface_description', models.CharField(default='', max_length=128, verbose_name='前置接口描述')),
                ('case_fan', models.CharField(default='', max_length=128, verbose_name='机箱风扇')),
                ('internal_heat_dissipation_description', models.CharField(default='', max_length=128, verbose_name='内部散热描述')),
                ('support_water_cooling', models.BooleanField(default=False, verbose_name='支持水冷')),
                ('GPU_length_limit', models.IntegerField(blank=True, null=True, verbose_name='显卡限长')),
                ('radiator_height_limit', models.IntegerField(blank=True, null=True, verbose_name='散热器限高')),
                ('power_location', models.CharField(default='', max_length=64, verbose_name='电源位置')),
                ('support_back_routing', models.BooleanField(default=False, verbose_name='支持背部走线')),
                ('case_size', models.CharField(default='', max_length=64, verbose_name='机箱尺寸')),
                ('other_properties', models.CharField(default='', max_length=128, verbose_name='其它性能')),
            ],
            options={
                'verbose_name': '机箱信息',
                'verbose_name_plural': '机箱信息',
            },
        ),
    ]
