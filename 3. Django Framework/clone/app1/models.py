
from django.db import models

class Materi(models.Model):
    id = models.CharField(max_length=80, null=False, primary_key=True)
    name = models.CharField(max_length=90, null=True)
    level = models.CharField(max_length=90, null=True)
    
class Peserta(models.Model):
    id = models.CharField(max_length=80, null=False, primary_key=True)
    name = models.CharField(max_length=90, null=True)
    gender = models.CharField(max_length=90, null=True)
    age = models.IntegerField(default=10)

class DaftarPeserta(models.Model):
    id = models.CharField(max_length=80, null=False, primary_key=True)
    peserta = models.ForeignKey(Peserta, null=True, on_delete=models.SET_NULL)
    materi = models.ForeignKey(Materi, null=True, on_delete=models.SET_NULL)
