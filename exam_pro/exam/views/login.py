#!/usr/bin/env python
# encoding: utf-8

# *****************************
# @Time      : 18-6-6 下午7:38
# @Author    : BaiFengQing
# @FileName  : login.py
# @Software  : PyCharm
# *****************************


from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from exam import models
# from rest_framework.views import APIView


class LoginView(View):


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
        id_number = request.POST.get('id_number')
        user_obj = models.Examinee.objects.filter(idCard=id_number).first()
        # if not user_obj:
        #     return render(request,'exam/login.html',{'error_msg':'身份证有误,请重试'})

        return render(request,'exam/face_auth.html')