from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import logging
import json
import datetime

logging.basicConfig(level=logging.DEBUG)

def index(request):
    return HttpResponse("Welcome to Once studio")
