from django import forms

#form fields en django: https://docs.djangoproject.com/en/1.11/ref/forms/fields/

class nuevo_academico_form(forms.Form):
	nombre=forms.CharField(label="nombre");
	apellido=forms.CharField(label="apellido");
	rut=forms.CharField(label="rut");
	#asignaturas=forms.MultipleChoiceField(widget=forms.SelectMultiple);