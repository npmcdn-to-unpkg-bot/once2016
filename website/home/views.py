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


def getphoto_action(request, question_id):
    #question = get_object_or_404(Question, pk=question_id)
    try:
    	pass

        #selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
    	pass
    	'''
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
        '''
      
    else:
    	return HttpResponseRedirect(reverse('home:getphoto_result', args=(question_id,)))
    	'''
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        '''


def getphoto_result(request, question_id):
	#def results(request, question_id):
    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/results.html', {'question': question})
    if question_id == 11:
        context = {"message": "ok, get your image"}
    else:
        context = {"message": "you can not get the image"}
    return render(request, 'getphoto_result.html', context)