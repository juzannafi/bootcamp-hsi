from django.http import HttpResponse
from django.shortcuts import render
from projecthsi.model import Participant

def index(response):
    return HttpResponse("Welcome")

def participant(request):
    list_participant = Participant.objects.all()
    # print(list_participant) #debug
    data = {'list_participant' : list_participant}
    return render(request, 'participant.html', context=data)