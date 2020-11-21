from django.http import HttpResponse, JsonResponse
from app1.models import Peserta

def fungsi_satu(request):
    return HttpResponse("Bismillaah")

def get_list_peserta(request):
    list_peserta = []
    for p in Peserta.objects.filter(): # SELECT ALL
        # print(p)
        list_peserta.append({
            'name': p.name,
            'gender' : p.gender
        })
    return list_peserta

def fungsi_dua(request):
    list_peserta = get_list_peserta(request)
    data = {
        'status' : 'ok',
        'msg' : 'Bismillaah'
    }
    return JsonResponse(data)

def fungsi_tiga(request):
    return HttpResponse(f"""
        <h1>Bismillah</h1>
        <h2>Ahlan wa sahlan</h2>
    """)