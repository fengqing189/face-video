# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-18 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_number', models.IntegerField(verbose_name='座位编号')),
                ('idCard', models.IntegerField(db_index=True, verbose_name='考生身份证')),
                ('current_pic', models.CharField(max_length=255, verbose_name='实时图片存放路径')),
            ],
        ),
        migrations.CreateModel(
            name='Examinee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCard', models.IntegerField(db_index=True, verbose_name='考生身份证号码')),
                ('stard_pic', models.CharField(max_length=255, verbose_name='考生标准照存放路径')),
            ],
        ),
        migrations.CreateModel(
            name='Recard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_number', models.IntegerField(verbose_name='座位编号')),
                ('idCard', models.IntegerField(db_index=True, verbose_name='考生身份证')),
                ('current_pic', models.CharField(max_length=255, verbose_name='实时图片存放路径')),
                ('is_login', models.BooleanField(verbose_name='是否是登录照片')),
                ('is_body', models.IntegerField(choices=[(1, '是'), (2, '否')], null=True, verbose_name='是否有人')),
                ('oneself', models.IntegerField(choices=[(1, '是'), (2, '否')], null=True, verbose_name='是否是本人')),
                ('turn', models.IntegerField(choices=[(1, '是'), (2, '否')], null=True, verbose_name='是否转头')),
                ('up_head', models.IntegerField(choices=[(1, '是'), (2, '否')], null=True, verbose_name='是否抬头')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]