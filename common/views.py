# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *

# Create your views here.
def index(request):
    return render(request,'common/index.html')

def index_cargas(request):
	return render(request,'common/cargas/index.html')

def index_academicos(request):
	academicos=Academico.objects.all();
	context={
		'academicos':academicos,
	}
	return render(request,'common/academicos/index.html',context)

def index_asignaturas(request):
	asignaturas=Asignatura.objects.all();
	context={
		'asignaturas':asignaturas,
	}
	return render(request,'common/asignaturas/index.html',context)


def registro_academicos(request):
	return HttpResponse("Registro academicos")

def registro_cargas(request,id_academico):
	return HttpResponse("Registro cargas academico_id={0}".format(id_academico))


def registro_asignaturas(request):
	return render(request,'common/asignaturas/new.html')


def editar_academicos(request,id):
	return HttpResponse("Editar academicos id_academico={0}".format(id))


def editar_cargas(request,id_academico):
	return HttpResponse("Editar cargas id_academico ={0}".format(id_academico))

def editar_asignaturas(request,id):
	return HttpResponse("Editar asignaturas id_asignatura={0}".format(id))
