from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse,HttpResponse
from devops.models import *
import json



def user_info(request):
    # 调用request.META（元数据方法）
    # print(request.META)
    # 获取用户端的ip地址
    ip_addr = request.META['REMOTE_ADDR']
    # 获取用户端的浏览器信息
    user_ua = request.META['HTTP_USER_AGENT']
    print(len(user_ua),user_ua)
    user_obj = UserIPInfo.objects.filter(ip = ip_addr)
    if len(user_obj)==0:
        print("empty")
        res = UserIPInfo.objects.create(ip = ip_addr)
        ip_addr_id = res.id
    else:
        ip_addr_id = user_obj[0].id
        print(ip_addr_id)

    BrowerInfo.objects.create(useragent=user_ua,userip_id=ip_addr_id)
    result = {

        'status':'success',
        'INFO':'User info',
        'IP':ip_addr,
        'UA':user_ua,
    }

    return HttpResponse(json.dumps(result),content_type="application/json")
