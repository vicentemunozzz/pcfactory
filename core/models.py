from django.db import models

class PARTNER(models.Model):

    USU_RUT = models.CharField(primary_key=True,max_length=13)
    USU_NOMBRE = models.CharField(max_length=30)
    USU_APELLIDO = models.CharField(max_length=30)
    USU_CORREO = models.CharField(max_length=100)
    USU_CONTRASENIA = models.CharField(max_length=100)
    objects = models.Manager()

    
    
    
  