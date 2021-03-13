from django.db import models

class Post(models.Model):
	personaje = models.TextField(default = "")
	descripcion = models.TextField(default = "")
	fecha = models.TextField(default = "")

	def __str__ (self):
		return self.personaje