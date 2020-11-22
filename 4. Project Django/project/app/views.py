from django.http import HttpResponse
from django.shortcuts import render
from app.model import Peserta

def index(request):
    return HttpResponse("Welcome")

def peserta(request):
    list_peserta = Peserta.objects.all()
    # print(list_peserta) #debug
    data = {'list_peserta' : list_peserta}
    return render(request, 'peserta.html', context=data)

def peserta_tabel(request):
    list_peserta = Peserta.objects.all()
    # print(list_peserta)  # debug
    data = {'list_peserta': list_peserta}
    return render(request, 'peserta_tabel.html', context=data)