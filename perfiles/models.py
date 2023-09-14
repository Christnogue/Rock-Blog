from django.db import models
from django.utils import timezone

class Profile(models.Model):
    nombre = models.CharField(max_length=200, default='')
    apellidos = models.CharField(max_length=200, default='')  
    correo = models.EmailField(default='')
    
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, default='')
 
    
