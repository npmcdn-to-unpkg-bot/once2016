#!/usr/bin/env python
# -*- coding: utf=8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render 
from django.shortcuts import render_to_response
from django.conf import settings
from django import forms

import logging
import json
import datetime

from .models import UserPhoto
from .models import Appointment

logging.basicConfig(level=logging.DEBUG)

from django.contrib.admin.views.decorators import staff_member_required


def index(request):
    context = {}
    return render(request, 'index.html', context)
    #return HttpResponse("Welcome to Once studio")

def about(request):
	context = {}
	return render(request, 'about.html', context)

def public_photos(request):
	context = {}
	return render(request, 'public_photos.html', context)

def user_photo(request):
	context = {}
	return render(request, 'user_photo.html', context)


def user_photo_result(request):
    user_name = request.POST.get("user_name", "")
    user_phone = request.POST.get("user_phone", "")
    access_code = request.POST.get("access_code", "")
    
    if user_name and user_phone and access_code:
        try:
            user_photo  = UserPhoto.objects.get(user_name=user_name, user_phone=user_phone, access_code=access_code)
            context = {"success": True, "message": "认证通过，返回照片", "photo_name": user_photo.photo_name}
        except UserPhoto.DoesNotExist:
            context = {"success": False, "message": "账号或者访问码错误"}
    else:
		context = {"success": False, "message": "信息不全，无法获取照片"}

    return render(request, 'user_photo_result.html', context)


def appointment(request):
    context = {}
    return render(request, 'appointment.html', context)


def appointment_result(request):
    user_name = request.POST.get("user_name", "")
    user_phone = request.POST.get("user_phone", "")
    user_email = request.POST.get("user_email", "")
    photo_type = request.POST.get("photo_type", "")
    photo_people_number = request.POST.get("photo_people_number", "")
    appointment_date = request.POST.get("appointment_date", "") # 2016-08-03
    appointment_time = request.POST.get("appointment_time", "") # time3
    
    if user_name and user_phone and user_email and photo_type and photo_people_number and appointment_date and appointment_time:
        try:   
            if Appointment.objects.filter(appointment_date=appointment_date, appointment_time=appointment_time).exists():
                context = {"success": False, "message": "该时间段已有预约，请重新选择预约时间"}
            else:
                appointment = Appointment(user_name=user_name, user_phone=user_phone, user_email=user_email, photo_type=photo_type, photo_people_number=photo_people_number, appointment_date=appointment_date, appointment_time=appointment_time)
                appointment.save()
                context = {"success": True, "message": "恭喜你，成功预约", "appointment": appointment}

        except Exception as e:
            context = {"success": False, "message": "预约失败，错误信息: " + str(e)}
    else:
        context = {"success": False, "message": "信息不全，预约失败"}

    return render(request, 'appointment_result.html', context)


class ImageForm(forms.Form):
    image = forms.FileField()


def save_file(file, path=''):
    filename = file._get_name()
    fd = open('%s/%s' % (settings.MEDIA_ROOT, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()


# Refer to https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#the-staff-member-required-decorator
@staff_member_required
def once_manage(request):
    form = ImageForm()
    appointments = Appointment.objects.order_by('-id')[:50]
    user_photos = UserPhoto.objects.order_by('-id')[:50]

    # Request to upload file
    if request.method == 'POST':
        user_name = request.POST.get("user_name", "")       
        user_phone = request.POST.get("user_phone", "")
        access_code = request.POST.get("access_code", "")
     
        if user_name and user_phone and access_code:
            try:
                # Ignore if the instance exists
                if UserPhoto.objects.filter(user_name=user_name, user_phone=user_phone, access_code=access_code).exists():
                    context = {"success": False, "message": "照片信息完全重复，不能上传", "appointments": appointments, "user_photos": user_photos, "form": form}
                else:
                    # Upload and save locally
                    form = ImageForm(request.POST, request.FILES)
                    if form.is_valid() and form.is_multipart():
                        save_file(request.FILES['image'])

                        photo_name = str(request.FILES['image']._get_name())
                        user_photo  = UserPhoto(user_name=user_name, user_phone=user_phone, access_code=access_code, photo_name=photo_name)
                        user_photo.save()
                        context = {"success": True, "message": "成功上传并保存到数据库", "appointments": appointments, "user_photos": user_photos, "form": form}
            except Exception as e:
                context = {"success": False, "message": "失败，错误日志" + str(e), "appointments": appointments, "user_photos": user_photos, "form": form}

        else:
            context = {"success": False, "message": "信息不全，不能上传", "appointments": appointments, "user_photos": user_photos, "form": form}

    # Request to access once manage page
    elif request.method == 'GET':
        context = {
            "appointments": appointments,
            "user_photos": user_photos,
            "form": form,
        }

    return render(request, 'once_manage.html', context)




from weixin import handler as HD
from weixin.backends.dj import Helper, sns_userinfo
from weixin import WeixinHelper, JsApi_pub, WxPayConf_pub, UnifiedOrder_pub, Notify_pub, catch

import json
import time
import random
import hashlib
from urllib import quote

from weixin.config import WxPayConf_pub
from weixin.lib import HttpClient, WeixinHelper


@sns_userinfo
def pay(request):
    response = render_to_response("pay.html")
    response.set_cookie("openid", Helper.sign_cookie(request.openid))
    return response

@sns_userinfo
@catch
@csrf_exempt
def paydetail(request):
    # Verify signature http://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=jsapisign
    """获取支付信息"""
    openid = request.openid
    money = request.POST.get("money") or "0.01"
    money = int(float(money)*100)

    jsApi = JsApi_pub()
    unifiedOrder = UnifiedOrder_pub()
    unifiedOrder.setParameter("openid",openid) #商品描述
    unifiedOrder.setParameter("body","充值测试") #商品描述
    timeStamp = time.time()
    out_trade_no = "{0}{1}".format(WxPayConf_pub.APPID, int(timeStamp*100))
    unifiedOrder.setParameter("out_trade_no", out_trade_no) #商户订单号
    unifiedOrder.setParameter("total_fee", str(money)) #总金额
    unifiedOrder.setParameter("notify_url", WxPayConf_pub.NOTIFY_URL) #通知地址 
    unifiedOrder.setParameter("trade_type", "JSAPI") #交易类型
    unifiedOrder.setParameter("attach", "6666") #附件数据，可分辨不同商家(string(127))


    try:
        prepay_id = unifiedOrder.getPrepayId()
        jsApi.setPrepayId(prepay_id)
        jsApiParameters = jsApi.getParameters()
    except Exception as e:
        print(e)
    else:
        print jsApiParameters
        return HttpResponse(jsApiParameters)


FAIL, SUCCESS = "FAIL", "SUCCESS"
@catch
def payback(request):
    """支付回调"""
    xml = request.raw_post_data
    #使用通用通知接口
    notify = Notify_pub()
    notify.saveData(xml)
    print xml
    '''
     {"package": "prepay_id=wx20160825222035bef438f0c60078733891", 
    "timeStamp": "1472134835", "signType": "MD5", 
    "paySign": "7F99E8E5137EA588572CC1BF982617BF", 
    "appId": "wx75977e365985b919", 
    "nonceStr": "wg62p8jgnrcri526x8bah1ldtx7tvlh0"}
    '''

    #验证签名，并回应微信。
    #对后台通知交互时，如果微信收到商户的应答不是成功或超时，微信认为通知失败，
    #微信会通过一定的策略（如30分钟共8次）定期重新发起通知，
    #尽可能提高通知的成功率，但微信不保证通知最终能成功
    if not notify.checkSign():
        notify.setReturnParameter("return_code", FAIL) #返回状态码
        notify.setReturnParameter("return_msg", "签名失败") #返回信息
    else:
        result = notify.getData()

        if result["return_code"] == FAIL:
            notify.setReturnParameter("return_code", FAIL)
            notify.setReturnParameter("return_msg", "通信错误")
        elif result["result_code"] == FAIL:
            notify.setReturnParameter("return_code", FAIL)
            notify.setReturnParameter("return_msg", result["err_code_des"])
        else:
            notify.setReturnParameter("return_code", SUCCESS)
            out_trade_no = result["out_trade_no"] #商户系统的订单号，与请求一致。
            ###检查订单号是否已存在,以及业务代码(业务代码注意重入问题)

    return  HttpResponse(notify.returnXml())

