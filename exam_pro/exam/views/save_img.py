
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from exam import models
import json
import os
import base64
import time


class LoginSaveImg(View):

    def post(self,request,*args,**kwargs):
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        id_card = request.COOKIES.get('id_card')
        print(id_card)

        img_b64 = request.POST.get('img_b64')
        img_b64 = img_b64.split(",")[1]
        imgdata = base64.b64decode(img_b64)

        base_path = '/face/current_img/'
        second_folder = str(ip)
        ip_list = os.listdir(base_path)
        if second_folder in ip_list:
            img_path = base_path + second_folder + '/'
        else:
            os.mkdir(base_path+second_folder)
            img_path = base_path + second_folder + '/'

        name = str(int(time.time()))+'.png'
        img_save_path = img_path + name
        with open(img_save_path,'wb') as f:
            f.write(imgdata)

        models.Record.objects.create(site_number=second_folder,idCard=id_card,current_pic=img_save_path,)

        return HttpResponse(json.dumps({'info':"success"}))