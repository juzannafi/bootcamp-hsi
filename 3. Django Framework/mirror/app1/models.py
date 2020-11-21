
from django.db import models

class Peserta(models.Model):
    name = models.CharField(max_length=90, null=True)
    gender = models.CharField(max_length=90, null=True)
    age = models.IntegerField(default=10)

