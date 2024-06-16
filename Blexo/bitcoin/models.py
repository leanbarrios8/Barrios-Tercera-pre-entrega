from django.db import models

class Moneda(models.Model):
    nombre = models.CharField(max_length=20)
    valor = models.CharField(max_length=20)
    
    def __str__(self):
        return f'Soy la moneda: {self.nombre} {self.valor}'
    
