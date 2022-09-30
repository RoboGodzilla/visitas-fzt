from django.urls import path

from . import views

urlpatterns = [
    path('pais', views.tablapais, name='pais'),
    path('pais/registro', views.registropais, name='regpais'),
    path('pais/<uuid:id>/', views.detallepais, name='detpais'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    
    path('estado', views.tablaestado, name='estado'),
    path('estado/registro', views.registroestado, name='regestado'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('ciudad', views.tablaciudad, name='ciudad'),
    path('ciudad/registro', views.registrociudad, name='regciudad'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('usuarios', views.tablausuarios, name='usuarios'),
    path('usuarios/registro', views.registrousuario, name='regusuario'),

    path('roles', views.tablaroles, name='roles'),
    path('roles/registro', views.registrorol, name='regrol'),
]