#!/usr/bin/evn python 
# -*- coding: utf-8 -*-

# @Time    : 18-6-25 下午11:17
# @Author  : BaiFengQing
# @File    : exam_index.py
# @Software: PyCharm


# 用户登录成功,开始考试的页面
from django.shortcuts import render,redirect,HttpResponse
from django.views import View

class ExamIndex(View):

    def get(self,request,*args,**kwargs):

        return render(request,'exam/exam_index.html')