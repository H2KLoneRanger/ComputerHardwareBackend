# Generated by Django 3.2.10 on 2022-04-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128, verbose_name='内存名称')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='内存价格')),
                ('manufacturer', models.CharField(default='', max_length=128, verbose_name='制造厂方')),
                ('applicable_type', models.CharField(default='', max_length=64, verbose_name='适用类型')),
                ('memory_type', models.CharField(default='', max_length=64, verbose_name='内存类型')),
                ('memory_dominant_frequency', models.IntegerField(blank=True, null=True, verbose_name='内存主频')),
                ('total_memory_capacity', models.IntegerField(blank=True, null=True, verbose_name='内存总容量')),
                ('memory_capacity_description', models.CharField(default='', max_length=64, verbose_name='内存容量描述')),
                ('number_of_pins', models.CharField(default='', max_length=64, verbose_name='插脚数目')),
                ('working_sequence', models.CharField(default='', max_length=64, verbose_name='工作时序')),
                ('memory_voltage', models.CharField(default='', max_length=64, verbose_name='内存电压')),
            ],
            options={
                'verbose_name': '内存信息',
                'verbose_name_plural': '内存信息',
            },
        ),
    ]
