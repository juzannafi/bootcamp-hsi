



from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from app1.models import Peserta, Materi, DaftarPeserta


def get_daftarpeserta(request):

    qs = DaftarPeserta.objects.filter(materi__name='Data Science', peserta__gender='Laki-laki')
    print(qs.query)
    
    # dp = DaftarPeserta.objects.get(id=4)
    # dp.delete()

def get_list_peserta(request):
    list_peserta = []
    
    name = request.GET.get('name', '')
    age = request.GET.get('age', '')
    # name = request.POST.get('name', '')
    
    
    # qs = Peserta.objects.filter(gender='Laki-laki', age=10)
    qs = Peserta.objects.filter()
    
    if name:
        qs = Peserta.objects.filter(name__icontains=name)
    if age:
        qs = qs.filter(age=age)
    # print(qs.query)
    
    for p in qs:
        list_peserta.append({
            'name': p.name,
            'age': p.age,
            'gender': p.gender,
        })
        
    return list_peserta


def insert_materi():
  
  materi = Materi()
  materi.id = 2
  materi.name = "Pengenalan Django"
  materi.level = "Menengah"
  materi.save()


def update_materi():
  
  materi = Materi.objects.get(id=2)
  materi.name = "Data Science"
  materi.save()

def insert_daftarpeserta():
  
  dp = DaftarPeserta()
  dp.id = 1
  dp.materi_id = 2
  dp.peserta_id = 1
  dp.save()
  
  dp = DaftarPeserta()
  dp.id = 2
  dp.materi_id = 2
  dp.peserta_id = 2
  dp.save()

def fungsi_satu(request):
    # insert_materi()
    # update_materi()
    insert_daftarpeserta()
    return HttpResponse("Bismillaah")

def fungsi_dua(request):
    get_daftarpeserta(request)
    list_peserta = []#get_list_peserta(request)
    data = {'status': 'ok', 'msg': 'Bismillaah', 'list_peserta': list_peserta}
    return JsonResponse(data)

def fungsi_tiga(request):
    return HttpResponse(f"""
        <h1>Bismillaah</h1>
        <h2>Ahlan wa sahlan</h2>
    """)

def fungsi_empat(request):
    data = {
        'text1': 'Contoh teks1',
        'color': 'Merah',
        'list_peserta00': get_list_peserta(request),
    }
    return render(request, "listpeserta.html", data)




