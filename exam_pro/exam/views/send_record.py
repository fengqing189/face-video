#!/usr/bin/evn python 
# -*- coding: utf-8 -*-

# @Time    : 18-6-24 下午6:11
# @Author  : BaiFengQing
# @File    : send_record.py
# @Software: PyCharm

from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from db.redis_pool import Redis_POOL
from exam import models
import json
import redis
butch_size = 100


class AiTools(object):
    '''AI调用模块'''

    def data_request(self,butch_size):
        redis_conn = redis.Redis(connection_pool=Redis_POOL)
        is_exist = redis_conn.exists('face')  # redis中是否存在face键
        print(is_exist)
        if not is_exist:
            redis_conn.hset('face', 'record_num', 0)                   # 实时照片的处理到的节点
            redis_conn.hset('face', 'login_num', 0)                    # # 登录照片的处理到的节点
        if not redis_conn.hexists('face','record_num'):
            redis_conn.hset('face', 'record_num', 0)
        if not redis_conn.hexists('face','login_num'):
            redis_conn.hset('face', 'login_num', 0)

        login_num = eval(redis_conn.hget('face', 'login_num'))
        record_num = eval(redis_conn.hget('face', 'record_num'))

        login_query = models.Record.objects.filter(is_body=0,is_login=1).order_by("id")[login_num:100]
        login_send_num = len(login_query)                             # 当前这次要发送的登录的记录条数
        rest_num = butch_size - login_send_num                        # 当前这次要发送的实时图像的记录条数

        record_query = models.Record.objects.filter(is_body=0).exclude(is_login=1)[record_num:rest_num]

        dest_data = []

        for login_obj in login_query:
            login_tmp = []
            login_id = login_obj.id
            login_path = login_obj.current_pic
            login_is_login = 1
            login_tmp.extend([login_id,login_path,login_is_login])
            dest_data.append(login_tmp)

        for record_obj in record_query:
            record_tmp = []
            record_id = record_obj.id
            record_path = record_obj.current_pic
            record_is_login = 0
            record_tmp.extend([record_id,record_path,record_is_login])
            dest_data.append(record_tmp)

        new_login_num = login_num + login_send_num
        new_record_num = record_num + len(record_query)

        redis_conn.hset('face','login_num',new_login_num)
        redis_conn.hset('face','record_num',new_record_num)
        print('next login',new_login_num)
        print('next record',new_record_num)
        return dest_data


class SendRecad(View):
    '''AI接口'''

    def get(self,request,*args,**kwargs):

        ai_tools = AiTools()
        ret = ai_tools.data_request(100)
        print('返回的结果是:',ret)

        return HttpResponse(json.dumps({"send_card":'ok'}))