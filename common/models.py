# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Asignatura(models.Model):
	nombre=models.CharField(max_length=200)
	codigo=models.CharField(max_length=200)
	def __unicode__(self):
		return self.codigo+" - "+self.nombre

class Academico(models.Model):
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	rut=models.CharField(max_length=20)
	asignaturas=models.ManyToManyField(Asignatura,blank=True)
	def __unicode__(self):
		return self.nombre+" "+self.apellido


class Carga(models.Model):
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	rut=models.CharField(max_length=20)
	academco = models.ForeignKey(Academico, on_delete=models.CASCADE,blank=True)
	def __unicode__(self):
		return self.nombre+" "+self.apellido




