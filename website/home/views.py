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

def getphoto(request):
	context = {}
	return render(request, 'getphoto.html', context)


def getphoto_result(request):
    user_name = request.POST.get("user_name", "")
    user_phone = request.POST.get("user_phone", "")
    access_code = request.POST.get("access_code", "")
    
    if user_name and user_phone and access_code:
        try:
            user_photo  = UserPhoto.objects.get(user_name=user_name, user_phone=user_phone, access_code=access_code)
            context = {"authorize": True, "message": "ok, get your image", "photo_name": user_photo.photo_name}
        except UserPhoto.DoesNotExist:
            context = {"authorize": False, "message": "user name or access code error"}
    else:
		context = {"authorize": False, "message": "you are not allowed get the image"}

    return render(request, 'getphoto_result.html', context)


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
                context = {"success": False, "message": "some one have made appointment at that time"}
            else:
                appointment = Appointment(user_name=user_name, user_phone=user_phone, user_email=user_email, photo_type=photo_type, photo_people_number=photo_people_number, appointment_date=appointment_date, appointment_time=appointment_time)
                appointment.save()
                context = {"success": True, "message": "ok, success to record the appointment", "appointment": appointment}

        except Exception as e:
            context = {"success": False, "message": "fail to record the assignment" + str(e)}
    else:
        context = {"success": False, "message": "need more info to record assignment"}

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




