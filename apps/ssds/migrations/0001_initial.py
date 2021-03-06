# Generated by Django 3.2.10 on 2022-04-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SSD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, verbose_name='固态硬盘名称')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='固态硬盘价格')),
                ('manufacturer', models.CharField(default='', max_length=128, verbose_name='制造厂方')),
                ('capacity', models.IntegerField(blank=True, null=True, verbose_name='固态硬盘容量')),
                ('cache_capacity', models.IntegerField(blank=True, null=True, verbose_name='缓存容量')),
                ('flash_type', models.CharField(default='', max_length=64, verbose_name='闪存类型')),
                ('max_continuous_read_speed', models.IntegerField(blank=True, null=True, verbose_name='连续读取最大速度')),
                ('max_continuous_write_speed', models.IntegerField(blank=True, null=True, verbose_name='连续写入最大速度')),
                ('disk_size', models.CharField(default='', max_length=64, verbose_name='硬盘尺寸')),
                ('interface_type', models.CharField(default='', max_length=64, verbose_name='接口类型')),
            ],
            options={
                'verbose_name': '固态硬盘信息',
                'verbose_name_plural': '固态硬盘信息',
            },
        ),
    ]
