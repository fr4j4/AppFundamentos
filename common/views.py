# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.utils.html import escape
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader

from .models import *
from .formulariosWeb import *
import json
#from django.utils import simplejson
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
	#POST - recibir un ajax con toda la informacion
	elif(request.method=='POST'):
		return HttpResponse("Oops")
		'''
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
			
			cargas=request.POST.getlist('cargas[]')
			return HttpResponse(request.body)
		else:
			return HttpResponse("problemas con el formulario");
			'''
	else:
		pass

def registro_academicos_ajax(request):
	if(request.is_ajax()):
		#jinput=json.loads(request.body)
		jinput=json.loads(request.body)
		if(validateJSON(jinput)):
			academico=Academico()
			academico.nombre=jinput['academico']['nombre']
			academico.apellido=jinput['academico']['apellido']
			academico.rut=jinput['academico']['rut']
			academico.save();
			for i in jinput['asignaturas']:
				asig_id=i
				asignatura=Asignatura.objects.get(id=asig_id)
				academico.asignaturas.add(asignatura);
			for i in jinput['cargas']:
				carga=Carga(academco=academico)
				carga.nombre=i['nombre']
				carga.apellido=i['apellido']
				carga.rut=i['rut']
				carga.save()

			return JsonResponse({"result":"yes"})
		else:
			return JsonResponse({"result":"NO"})
	else:
		return HttpResponse("Get out!")

def editar_academico_ajax(request):
	if(request.is_ajax()):
		jinput=json.loads(request.body)
		if(validateJSON(jinput)):
			academico=Academico.objects.get(id=jinput['academico']['id'])
			academico.nombre=jinput['academico']['nombre']
			academico.apellido=jinput['academico']['apellido']
			academico.rut=jinput['academico']['rut']
			academico.save();
			for c in Carga.objects.filter(academco=academico):
				c.delete()
			
			academico.asignaturas.clear()
			

			for i in jinput['asignaturas']:
				asig_id=i
				asignatura=Asignatura.objects.get(id=asig_id)
				academico.asignaturas.add(asignatura);
			for i in jinput['cargas']:
				carga=Carga(academco=academico)
				carga.nombre=i['nombre']
				carga.apellido=i['apellido']
				carga.rut=i['rut']
				carga.save()

			return JsonResponse({"result":"yes"})
		else:
			return JsonResponse({"result":"NO"})
	else:
		return HttpResponse("Get out!")

def validateJSON(_json):
	valido =True
	if(not _json['academico']['nombre'] or
		not _json['academico']['apellido'] or
		not _json['academico']['rut']):
		valido=False;
	else:
		for i in _json['cargas']:
			carga=Carga()
			carga.nombre=i['nombre']
			carga.apellido=i['apellido']
			carga.rut=i['rut']
			'''
			print "nombre: ",carga['nombre']
			print "apellido: ",carga['apellido']
			print "rut: ",carga['rut']
			'''
			if(not carga.nombre or
			   not carga.apellido or
			   not carga.rut
			):
				valido=False
				break

	return valido

def editar_academicos(request,id):
	if request.method=='GET':
		academico=Academico.objects.get(id=id)

		asignaturas=Asignatura.objects.all()
		cargas=Carga.objects.filter(academco=academico)
		for a in asignaturas:
			for b in academico.asignaturas.all():
				if a.id==b.id:
					a.dicta=True

		context={
			'academico':academico,
			'asignaturas':asignaturas,
			'cargas':cargas
		}
		return render(request,'common/academicos/editar.html',context)
	else:
		return HttpResponse("Metodo http no soportado, usar POST")

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


