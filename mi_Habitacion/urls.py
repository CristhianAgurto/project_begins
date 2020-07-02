from django.contrib import admin
from django.urls import path
from .views import room_stuff, home_view, room, fecha_actual 

urlpatterns = [ 
   path('cuarto/cosas', room_stuff , name="cosas"),
   path('', home_view),
   path('cuarto/', room),
   path('fecha/', fecha_actual)
]	