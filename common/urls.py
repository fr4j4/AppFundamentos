from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_common'),
    
    url(r'^academicos/$', views.index_academicos, name='acad'),
    url(r'^academicos/registrar/$', views.registro_academicos, name='acad_reg'),
    url(r'^academicos/(?P<id>\d+)/editar/$', views.editar_academicos, name='acad_edit'),
    url(r'^academicos/(?P<id>\d+)/eliminar/$', views.eliminar_academicos, name='acad_del'),
    
    url(r'^asignaturas/$', views.index_asignaturas, name='asig'),
    url(r'^asignaturas/registrar/$', views.registro_asignaturas, name='asig_nuevo'),
    url(r'^asignaturas/(?P<id>\d+)/editar/$', views.editar_asignaturas, name='asig_edit'),
    url(r'^asignaturas/(?P<id>\d+)/eliminar/$', views.eliminar_asignatura, name='asig_del'),

    #url(r'^academicos/cargas/$', views.index_cargas, name='carg'),
    #url(r'^academicos/(?P<id_academico>\d+)/cargas/registrar/$', views.registro_cargas, name='carg_reg'),
    #url(r'^academicos/(?P<id_academico>\d+)/cargas/editar/$', views.editar_cargas, name='carg_edit'),
    
    #usando ajax
    url(r'^ajax/academicos/registrar/$', views.registro_academicos_ajax, name='acad_reg_ajax'),
    url(r'^ajax/academicos/editar/$', views.editar_academico_ajax, name='acad_edit_ajax'),
]