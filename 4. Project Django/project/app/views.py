from django.http import HttpResponse
from function import insert_peserta

def index(request):
    return HttpResponse("Welcome")

def peserta(request):
    # users_list = Peserta.objects.all()
    # mydict
    # return
    insert_peserta(request)
    return HttpResponse("Daftar Peserta")