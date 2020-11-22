from django.db import models

class Peserta(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, default="Male")
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name