

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
