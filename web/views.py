from django.shortcuts import render
from .models import Tarea, Categoria, subTarea,Dia
# Create your views here.

def index(request):
    tareas = Tarea.objects.all()
    context = {
        'tareas': tareas
    }
    return render(request, 'index.html',context)

def tarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    subtareas = subTarea.objects.filter(tarea=tarea)
    context = {
        'tarea': tarea,
        'subtareas': subtareas    }
    return render(request, 'tarea.html', context)

def creartarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        dia = request.POST.get('dia')
        categoria = request.POST.get('categoria')
        subtarea = request.POST.get('subtarea')
        
        dia = Dia.objects.get(pk=dia) if dia else None
        categoria = Categoria.objects.get(pk=categoria) if categoria else None
        
        tarea = Tarea.objects.create(titulo=titulo, dia=dia, categoria=categoria)        
        if subtarea:
            subtarea = subTarea.objects.create(tarea=tarea, titulo=subtarea)
    
    
    dias = Dia.objects.all()
    categorias = Categoria.objects.all()
    context = {
        'dias': dias,
        'categorias': categorias
    }
    return render(request,'crearTarea.html', context)
    


def categorias(request):
    return render(request, 'categorias.html')