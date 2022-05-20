from django.db import models
#tabla de base de datos una clase por tabla
# Create your models here.
class Persona(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender= models.CharField(max_length=100)
    age= models.IntegerField()
    birthdate=models.DateField()
    relation=models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100)
