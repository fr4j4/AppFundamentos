from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    url(r'^academicos/registrar/$', views.registro_academicos, name='acad_reg'),
    url(r'^academicos/editar/(?P<id>\d+)/$', views.editar_academicos, name='acad_edit'),
    
    url(r'^asignaturas/registrar/$', views.registro_asignaturas, name='asig_reg'),
    url(r'^asignaturas/editar/(?P<id>\d+)/$', views.editar_asignaturas, name='asig_edit'),

    url(r'^academicos/(?P<id_academico>\d+)/cargas/registrar/$', views.registro_cargas, name='carg_reg'),
	url(r'^academicos/(?P<id_academico>\d+)/cargas/editar/$', views.editar_cargas, name='carg_edit'),
    
]