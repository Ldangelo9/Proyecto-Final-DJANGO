from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Equipo
from inicio.form import FormularioCrearEquipo 
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    
    return render(request, 'inicio/inicio.html')

@login_required
def crear_equipo(request):
    
    if request.method == "POST":
        formulario = FormularioCrearEquipo(request.POST, request.FILES)
        if formulario.is_valid():
            procesador = formulario.cleaned_data.get('procesador')
            ram = formulario.cleaned_data.get('ram')
            mother = formulario.cleaned_data.get('mother')
            video = formulario.cleaned_data.get('video')
            gabinete = formulario.cleaned_data.get('gabinete')
            imagen = formulario.cleaned_data.get('imagen')
           
            equipo = Equipo(procesador=procesador, ram=ram, mother=mother, video=video, gabinete=gabinete, imagen=imagen)
            equipo.save()
            
            return redirect("lista_equipos")
    else: 
        formulario = FormularioCrearEquipo()
    
    
    return render(request, 'inicio/crear_equipo.html', {'formulario': formulario})  

def lista_equipos(request):
    
    equipo = Equipo.objects.all()
    
    return render(request,'inicio/lista_equipos.html',{'lista_equipos': equipo})

def detalle_equipos(request, equipo_id):
    
    equipo = Equipo.objects.get(id=equipo_id)
    
    return render(request, 'inicio/detalle_equipos.html', {'equipo': equipo})

    
class ActualizarEquipo(LoginRequiredMixin, UpdateView):
    model = Equipo
    template_name = "inicio/actualizar_equipos.html"
    fields = "__all__"
    success_url = reverse_lazy('lista_equipos')
    
class EliminarEquipo(LoginRequiredMixin,DeleteView):
    model = Equipo
    template_name = "inicio/eliminar_equipos.html"
    success_url = reverse_lazy('lista_equipos')
    
def about_me (request):
    return render(request, 'inicio/about_me.html')