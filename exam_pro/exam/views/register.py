
# 考生注册视图

from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from exam import models

class ExamRegister(View):


    def get(self,request,*args,**kwargs):
        return render(request,'exam/register.html')


    def post(self,request):
        exam_name = request.POST.get("exam_name")
        exam_idcard = request.POST.get("exam_idcard")
        exam_img = request.FILES.get("exam_img")

        # 保存用户的照片到文件夹
        dest_img = '/face/card_img/'+str(exam_idcard) +'.jpg'
        with open(dest_img,'wb') as f_write:
            for chunk in exam_img.chunks():
                f_write.write(chunk)

        # 保存用户的信息到数据库
        obj = models.Examinee.objects.create(name=exam_name,idCard=exam_idcard,stard_pic=dest_img)
        print(obj,'已经写入数据库')
        return HttpResponse('考生档案添加成功')