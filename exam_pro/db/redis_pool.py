#!/usr/bin/evn python 
# -*- coding: utf-8 -*-

# @Time    : 18-6-24 下午6:20
# @Author  : BaiFengQing
# @File    : redis_pool.py
# @Software: PyCharm

import redis

Redis_POOL = redis.ConnectionPool(host="127.0.0.1", port=6379,) # redis线程池