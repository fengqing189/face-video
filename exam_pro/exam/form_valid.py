#!/usr/bin/env python
# encoding: utf-8

# *****************************
# @Time      : 18-6-6 下午8:31
# @Author    : BaiFengQing
# @FileName  : form_valid.py
# @Software  : PyCharm
# *****************************

from django import forms


class loginForm(forms.Form):

    id_number = forms.CharField(required=True,
                                max_length=18,
                                min_length=18,
                                error_messages={
                                    "require":"身份证必填",
                                    "max_length":'身份证需是18位',
                                    'min_length':'身份证需是18位',
                                })

    repeat_number = forms.CharField(required=True,
                                    max_length=18,
                                    min_length=18,
                                    error_messages={
                                        "require": "身份证必填",
                                        "max_length": '身份证需是18位',
                                        'min_length': '身份证需是18位',})

