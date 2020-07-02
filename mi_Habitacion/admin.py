from django.contrib import admin
from .models import Venta_garage


@admin.register(Venta_garage)
class Venta_garageAdmin(admin.ModelAdmin):
	
	list_display = ('id', 'articulo', 'precio')
	search_fields = ('articulo',)

# Register your models here.list_display = ('id', 'articulo', 'precio') -- search_fields = ('id',)
