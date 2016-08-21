

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render

import logging
import json
import datetime

from .models import UserPhoto
from .models import Appointment

logging.basicConfig(level=logging.DEBUG)

def index(request):
    context = {}
    return render(request, 'index.html', context)
    #return HttpResponse("Welcome to Once studio")

def about(request):
	context = {}
	return render(request, 'about.html', context)

def photos(request):
	context = {}
	return render(request, 'photos.html', context)

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

            appointment = Appointment(user_name=user_name, user_phone=user_phone, user_email=user_email, photo_type=photo_type, photo_people_number=photo_people_number, appointment_date=appointment_date, appointment_time=appointment_time)
            appointment.save()
            
            context = {"success": True, "message": "ok, success to record the appointment", "appointment": appointment}

        except Exception as e:
            context = {"success": False, "message": "fail to record the assignment" + str(e)}
    else:
        context = {"success": False, "message": "need more info to record assignment"}

    return render(request, 'appointment_result.html', context)
