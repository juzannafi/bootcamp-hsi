from django.db import models

# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=50)
    nip = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, default="Male")
    email = models.EmailField(unique=True)