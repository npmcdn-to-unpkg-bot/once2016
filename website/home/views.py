from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

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
	context = {"id": 10}
	# question = get_object_or_404(Question, pk=question_id)
	return render(request, 'getphoto.html', context)


def getphoto_result(request):

    #request.POST['choice']
    question_id = "10"

	#def results(request, question_id):
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/results.html', {'question': question})
    if question_id == "10":
        context = {"message": "ok, get your image", "question_id": question_id}
    else:
        context = {"message": "you can not get the image!!!", "question_id": question_id}
    return render(request, 'getphoto_result.html', context)