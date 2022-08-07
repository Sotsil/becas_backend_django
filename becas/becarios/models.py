from django.db import models

# Create your models here.

class Becario(models.Model):
    nombre = models.CharField(max_length= 56)
    correo = models.CharField(max_length= 56)
    pais = models.CharField(max_length= 56)
    status_beca = models.CharField(max_length= 56)
    area_estudio = models.CharField(max_length= 56)
    area_de_interes = models.CharField(max_length= 56)

    class Meta:
        db_table = 'becarios'

    def __str__(self):
        return self.nombre
        

