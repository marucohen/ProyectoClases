from django.db import models

# Create your models here.

class CategoriaClase(models.Model):
    nombre=models.CharField(max_length=60)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaClase"
        verbose_name_plural="categoriasClases"
    
    def __str__(self):
        return self.nombre

class ClaseProducto(models.Model):
    nombre= models.CharField(max_length=60)
    categorias=models.ForeignKey(CategoriaClase, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="pediTuClaseApp", null=True, blank=True)
    precio= models.FloatField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name="ClaseProducto"
        verbose_name_plural="ClasesProductos"
