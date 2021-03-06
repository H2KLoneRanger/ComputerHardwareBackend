# Generated by Django 3.2.10 on 2022-04-26 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='applicable_type',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='适用类型'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='manufacturer',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='制造厂方'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='memory_capacity_description',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='内存容量描述'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='memory_type',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='内存类型'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='memory_voltage',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='内存电压'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='name',
            field=models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='内存名称'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='number_of_pins',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='插脚数目'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='working_sequence',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='工作时序'),
        ),
    ]
