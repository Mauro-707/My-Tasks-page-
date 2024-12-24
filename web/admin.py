from django.contrib import admin
from .models import Tarea, Categoria, subTarea,Dia
# Register your models here.

admin.site.register(Tarea)
admin.site.register(Categoria)
admin.site.register(subTarea)
admin.site.register(Dia)