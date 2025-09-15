from django.db import models


class Equipo(models.Model):
    
    procesador = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)
    mother = models.CharField(max_length=20)
    video = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='equipos', null=True)
    
    def __str__(self):
        return f"{self.procesador} - {self.ram} - {self.mother} - {self.video}"