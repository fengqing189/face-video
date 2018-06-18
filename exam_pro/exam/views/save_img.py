
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from exam import models
import json
import os
import base64


class SaveImg(View):

    def post(self,request,*args,**kwargs):
        img_b64 = request.POST.get('img_b64')
        img_b64 = img_b64.split(",")[1]
        print(img_b64)
        imgdata = base64.b64decode(img_b64)


        with open('/12.png','wb') as f:
            f.write(imgdata)

        return HttpResponse(json.dumps({'info':"success"}))