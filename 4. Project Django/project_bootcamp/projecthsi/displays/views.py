from django.http import HttpResponse
from django.shortcuts import render
from displays.models import Participant

# Create your views here.
def index(request):
    return HttpResponse("Welcome Displays")

def participant(request):
    list_participant = Participant.objects.all()
    # print(list_participant) #debug
    data = {'list_participant': list_participant}
    return render(request, 'participant.html', context=data)

def participant_table(request):
    list_participant = Participant.objects.all()
    # print(list_participant) #debug
    data = {'list_participant': list_participant}
    return render(request, 'participant_table.html', context=data)

def add_participant(request):
    return render(request, 'add_participant.html')
