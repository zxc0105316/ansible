from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse,HttpResponse
from devops.models import  UserIPInfo,BrowerInfo
import json
from django.core.mail import send_mail
from devops.util.tools import sendmail


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


def user_history(request):
    ip_list = UserIPInfo.objects.all()
    print('&&&&&&&&&&&&&&&&&&&&&&',ip_list)
    infos = {}
    for item in ip_list:

        #   每一个ip对应的浏览器信息
        infos[item.ip] = [b_obj.useragent for b_obj in BrowerInfo.objects.filter(userip_id=item.id)]
        result = {
            "status": "success",
            "INFO":infos,
        }
    return HttpResponse(json.dumps(result),content_type="application/json")



def sendsmail(request):
            sendm = sendmail(receive_addr=['1207025339@qq.com'],sub_info="1",content_info="2")
            return HttpResponse(sendm.send())
            send_mail