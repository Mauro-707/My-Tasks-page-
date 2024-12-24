from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=50, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    dia = models.ForeignKey('Dia', on_delete=models.CASCADE, blank=True, null=True )

    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, blank=True, null=True )

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.titulo



class subTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50, blank=False)
    estado = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "subTarea"
        verbose_name_plural = "subsTareas"

    def __str__(self):
        return self.titulo



class Categoria(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre



class Dia(models.Model):
    nombre = models.CharField(blank=False, max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Dia"
        verbose_name_plural = "Dias"
        
    def __str__(self):
        return self.nombre
    