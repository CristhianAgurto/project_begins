from django.db import models
from django.utils import timezone

space = (
	("bedroom",'cuarto'),
	("kitchen",'cocina'),
	("garage",'garage'),
	("bathroom",'baño')
)
Estado = (
	("desgastado",'usado'),
	("maltratado",'funcional')
)

class Venta_garage(models.Model):

	articulo = models.CharField(max_length=200)
	precio = models.IntegerField()
	descripcion = models.TextField(blank=True, null=True, help_text="autor") 

	created_date = models.DateTimeField(
		default=timezone.now
	)

	published_date = models.DateTimeField(
		blank=True, null=True)

	
	is_active = models.BooleanField(default=False)
	

	tipy_fields = models.CharField(
		choices=space, blank=True, null=True, max_length=100)

	estado_stuff = models.CharField(
		choices=Estado, blank=True, null=True, max_length=100)

	
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__ (self):
		return '{}'.format(self.id)

class Order(models.Model):
	monto = models.IntegerField()
	def __str__(self):
		return u'Orden texto {} - {}'.format(self.id, self.monto)

# Create your models here.
