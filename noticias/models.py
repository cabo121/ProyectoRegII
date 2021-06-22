from django.db import models

class deportes (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	descripcion = models.CharField(default = "",null=True,max_length = 200)
	fuente = models.CharField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	imagen = models.ImageField(upload_to = "imagen" , null="True")

	def __str__ (self):
		return self.nombre


class corona (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	descripcion = models.CharField(default = "",null=True,max_length = 200)
	fuente = models.CharField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	imagen = models.ImageField(upload_to = "imagen" , null="True")

	def __str__ (self):
		return self.nombre


class nacionales (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	descripcion = models.CharField(default = "",null=True,max_length = 200)
	fuente = models.CharField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	imagen = models.ImageField(upload_to = "imagen" , null="True")

	def __str__ (self):
		return self.nombre
