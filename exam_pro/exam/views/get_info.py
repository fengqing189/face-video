
# AI请求当前每一帧的数据，返回当前数据库的数据
from rest_framework.views import APIView
from django.shortcuts import HttpResponse
import json

class GetCurrentInfo(APIView):

    def get(self,request,*args,**kwargs):


        return HttpResponse(json.dumps({'get info':'info'}))
