from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    estado = models.BooleanField(choices=[(True, 'Completada'), (False, 'Pendiente')], default=False)

    def __str__(self):
        return self.titulo