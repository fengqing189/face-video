#!/usr/bin/env python
# encoding: utf-8

# *****************************
# @Time      : 18-6-6 下午7:38
# @Author    : BaiFengQing
# @FileName  : login.py
# @Software  : PyCharm
# *****************************


from django.shortcuts import render,redirect,HttpResponse
from rest_framework.views import APIView


class LoginView(APIView):


    def get(self,request,*args,**kwargs):



        return render(request,'exam/login.html')

    def post(self,request,*args,**kwargs):
        '''
        考生提交证件号,去数据库查询该考生是否存在，存在则返回到视频检测页面，刷脸；不存在则返回重新登录
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''


        return render(request,'exam/face_auth.html')