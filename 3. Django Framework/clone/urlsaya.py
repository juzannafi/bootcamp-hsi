
from django.urls import path

from libsaya import fungsi_satu, fungsi_dua, fungsi_tiga, fungsi_empat

urlpatterns = [
    path('salam1', fungsi_satu),
    path('salam2', fungsi_dua),
    path('salam3', fungsi_tiga),
    path('salam4', fungsi_empat),
]

