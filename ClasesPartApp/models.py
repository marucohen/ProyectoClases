from django.db import models


# Create your models here.


class ClasesPart(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=60)
    imagen=models.ImageField(upload_to='ClasesPartApp')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='clase'
        verbose_name_plural= 'clases'
    
    def __str__(self):
        return self.titulo