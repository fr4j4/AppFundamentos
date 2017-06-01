# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.utils.html import escape
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import *
from .formulariosWeb import *
# Create your views here.

#metodos
#get: acceder por la url
#post: por formulario

def index(request):
    return render(request,'common/index.html')

def index_academicos(request):
	academicos=Academico.objects.all();
	context={
		'academicos':academicos,
	}
	return render(request,'common/academicos/index.html',context)

def registro_academicos(request):
	#GET
	if(request.method=='GET'):
		asignaturas=Asignatura.objects.all();
		context={
			'asignaturas':asignaturas
		}
		return render(request,'common/academicos/registrar.html',context)
	#POST
	elif(request.method=='POST'):
		formulario=nuevo_academico_form(request.POST)
		if formulario.is_valid():
			nombre=formulario.cleaned_data['nombre']
			apellido=formulario.cleaned_data['apellido']
			rut=formulario.cleaned_data['rut']
			asignaturas=request.POST.getlist('asignaturas')

			academico=Academico()
			academico.nombre=nombre
			academico.apellido=apellido
			academico.rut=rut
			academico.save()

			for asig_id in asignaturas:
				asignatura=Asignatura.objects.get(id=asig_id)
				academico.asignaturas.add(asignatura);

			return index_academicos(request)
		else:
			return HttpResponse("problemas con el formulario");
	else:
		pass

def editar_academicos(request,id):
	return HttpResponse("Editar academicos id_academico={0}".format(id))

################################################################################

def index_asignaturas(request):
	asignaturas=Asignatura.objects.all();
	context={
		'asignaturas':asignaturas,
	}
	return render(request,'common/asignaturas/index.html',context)

def registro_asignaturas(request):
	if(request.method=='POST'):
		pass
	else:
		pass

	return render(request,'common/asignaturas/new.html')

def editar_asignaturas(request,id):
	return HttpResponse("Editar asignaturas id_asignatura={0}".format(id))

################################################################################

def index_cargas(request):
	cargas=Carga.objects.all();
	context={
		'cargas':cargas,
	}
	return render(request,'common/cargas/index.html',context)

def registro_cargas(request,id_academico):
	return HttpResponse("Registro cargas academico_id={0}".format(id_academico))

def editar_cargas(request,id_academico):
	return HttpResponse("Editar cargas id_academico ={0}".format(id_academico))


