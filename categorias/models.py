from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class categorias(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank = True, null = True)
    estado = models.BooleanField(default= True)

    def __str__(self):
        return self.nombre