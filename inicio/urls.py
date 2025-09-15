from django.urls import path
from inicio.views import inicio, crear_equipo, lista_equipos, detalle_equipos, ActualizarEquipo, EliminarEquipo, about_me


urlpatterns = [
    path('', inicio, name='inicio'),
    path('equipos/', lista_equipos, name='lista_equipos'),
    path('equipos/crear/', crear_equipo, name='crear_equipo'),
    path('equipos/<equipo_id>/', detalle_equipos, name='detalle_equipos'),
    path('equipos/<pk>/actualizar', ActualizarEquipo.as_view(), name='actualizar_equipos'),
    path('equipos/<pk>/eliminar', EliminarEquipo.as_view(), name='eliminar_equipos'),
    path('about-me/', about_me, name='about_me'),
    
    ]