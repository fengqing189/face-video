from django.db import models


class Examinee(models.Model):
    '''考生表'''
    name = models.CharField(verbose_name='考生姓名',max_length=32,default='')
    idCard = models.CharField(verbose_name='考生身份证号码', db_index=True,max_length=32)
    stard_pic = models.CharField(verbose_name='考生标准照存放路径', max_length=255)


class Record(models.Model):
    '''实时照片记录表'''
    site_number = models.CharField(verbose_name='座位编号',max_length=32)
    idCard = models.CharField(verbose_name='考生身份证',max_length=32,db_index=True)
    current_pic = models.CharField(verbose_name='实时图片存放路径', max_length=255)   # 照片名称就是当前这一秒的时间戳
    status = ((1, '是'), (2, '否'))
    is_login = models.IntegerField(choices=status, verbose_name='是否登录', default=0)
    is_body = models.IntegerField(choices=status, verbose_name='是否有人', default=0)
    oneself = models.IntegerField(choices=status, verbose_name='是否是本人', default=0)
    turn = models.IntegerField(choices=status, verbose_name='是否转头', default=0)
    up_head = models.IntegerField(choices=status, verbose_name='是否抬头', default=0)


class ErrorInfo(models.Model):
    '''异常情况记录表'''
    site_number = models.CharField(verbose_name='座位编号',max_length=32)
    idCard = models.CharField(verbose_name='考生身份证', db_index=True,max_length=32)
    current_pic = models.CharField(verbose_name='实时图片存放路径', max_length=255)  # 照片名称就是当前这一秒的时间戳
