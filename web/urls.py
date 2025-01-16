from django.contrib import admin
from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index, name='index'),
    path('categorias/',views.categorias, name='categorias'),
    path('tarea/<int:tarea_id>',views.tarea, name='tarea'),
    path('creartarea/',views.creartarea, name='creartarea'),    
    path('eliminartarea/<int:tarea_id>',views.eliminartarea, name='eliminartarea'),
        
]
