from django.shortcuts import render
from django.shortcuts import get_object_or_404,redirect
from django.http import HttpResponse
from .models import Tarea, Categoria, subTarea,Dia
# Create your views here.

"""Obtener Tareas"""
def index(request):

    tareas = Tarea.objects.all()
    context = {
        'tareas': tareas
    }
    return render(request, 'index.html',context)

"""Obtener tarea por ID"""
def tarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    subtareas = subTarea.objects.filter(tarea = tarea)
    
    context = {
        'tarea': tarea,
        'subtareas': subtareas    }
    return render(request, 'tarea.html', context)

""" Crear Tareas """
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
    
def eliminartarea(request, tarea_id):
    if request.method == 'POST':
        tarea = get_object_or_404(Tarea,pk=tarea_id)
        tarea.delete()
        return redirect('web:index')

def editartarea(request,tarea_id):
    tarea = get_object_or_404(Tarea,pk=tarea_id)
    if request.method == 'POST':
        tarea.titulo = request.POST.get('titulo')
        tarea.dia = request.POST.get('dia')
        tarea.categoria = request.POST.get('categoria')
        tarea.save()

        #campos de subtareas
        titulos = request.POST.getlist('subtitulo')
        estado = request.POST.getlist('subestado')

        for titulo,estado in zip(titulos,estado):
            if titulo: #evita tareas vacias
                subTarea.objects.create(
                    tarea = tarea,
                    titulo = titulo,
                    estado = estado
                )

def categorias(request):
    return render(request, 'categorias.html')