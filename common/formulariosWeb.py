from django import forms

class nuevo_academico_form(forms.Form):
	nombre=forms.CharField(label="nombre");
	apellido=forms.CharField(label="apellido");
	rut=forms.CharField(label="rut");