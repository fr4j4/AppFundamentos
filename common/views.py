# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("COMMON.")

def registro_academicos(request):
	return HttpResponse("Registro academicos")

def registro_cargas(request,id_academico):
	return HttpResponse("Registro cargas academico_id={0}".format(id_academico))

def registro_asignaturas(request):
	return HttpResponse("Registro asignaturas")


def editar_academicos(request,id):
	return HttpResponse("Editar academicos id_academico={0}".format(id))

def editar_cargas(request,id_academico):
	return HttpResponse("Editar cargas id_academico ={0}".format(id_academico))

def editar_asignaturas(request,id):
	return HttpResponse("Editar asignaturas id_asignatura={0}".format(id))
