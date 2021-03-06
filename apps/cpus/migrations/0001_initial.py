# Generated by Django 3.2.10 on 2022-04-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, verbose_name='CPU名称')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='CPU价格')),
                ('manufacturer', models.CharField(default='', max_length=128, verbose_name='制造厂方')),
                ('series', models.CharField(default='', max_length=64, verbose_name='系列')),
                ('code_name', models.CharField(default='', max_length=64, verbose_name='核心代号')),
                ('total_cores', models.IntegerField(blank=True, null=True, verbose_name='内核数')),
                ('total_threads', models.IntegerField(blank=True, null=True, verbose_name='线程数')),
                ('sockets_supported', models.CharField(default='', max_length=64, verbose_name='插槽类型')),
                ('use_conditions', models.CharField(default='', max_length=64, verbose_name='使用类型')),
                ('architecture', models.CharField(default='', max_length=64, verbose_name='架构')),
                ('process_technology', models.CharField(default='', max_length=64, verbose_name='制程工艺')),
                ('base_frequency', models.IntegerField(blank=True, null=True, verbose_name='核心频率')),
                ('max_turbo_frequency', models.IntegerField(blank=True, null=True, verbose_name='最大睿频频率')),
                ('cache', models.IntegerField(blank=True, null=True, verbose_name='缓存')),
                ('compatible_mainboard', models.CharField(default='', max_length=128, verbose_name='兼容主板')),
                ('launch_date', models.IntegerField(blank=True, null=True, verbose_name='发行日期')),
                ('is_64bit', models.BooleanField(default=True, verbose_name='是否64位处理器')),
                ('processor_graphics', models.CharField(default='', max_length=128, verbose_name='处理器显卡')),
                ('max_memory_channels', models.IntegerField(blank=True, null=True, verbose_name='最大内存通道数')),
                ('memory_types', models.CharField(default='', max_length=128, verbose_name='支持内存类型')),
                ('TDP', models.IntegerField(blank=True, null=True, verbose_name='热功耗设计')),
            ],
            options={
                'verbose_name': 'CPU信息',
                'verbose_name_plural': 'CPU信息',
            },
        ),
    ]
