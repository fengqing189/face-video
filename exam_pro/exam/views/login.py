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
        if not user_obj:
            return render(request,'exam/login.html',{'error_msg':'证件输入有误,请重试'})

        # 确认考生在数据库之后，就把考生证件的路径，放到recard表中，并且is_login=1
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        models.Record.objects.create(site_number=ip,idCard=id_number,current_pic=user_obj.stard_pic,is_login=1)

        response = render(request,'exam/face_auth.html')
        response.set_cookie('id_card', id_number)
        return response
