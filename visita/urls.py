from django.urls import path

from . import views
from catalogo import views as catviews

urlpatterns = [
    path('escuela', views.tablaescuela, name='escuela'),
    path('escuela/registro', views.registroescuela, name='regescuela'),
    # path('<int:id>/', views.detail, name='detail'),
    # path('<int:id>/results/', views.results, name='results'),
    # path('<int:id>/vote/', views.vote, name='vote'),
    
    path('profesor', views.tablaprofesor, name='profesor'),
    path('profesor/registro', views.registroprofesor, name='regprofesor'),
    # path('<int:id>/', views.detail, name='detail'),
    # path('<int:id>/results/', views.results, name='results'),
    # path('<int:id>/vote/', views.vote, name='vote'),

    path('asesor', views.tablaasesor, name='asesor'),
    path('asesor/registro', views.registroasesor, name='regasesor'),
    # path('<int:id>/', views.detail, name='detail'),
    # path('<int:id>/results/', views.results, name='results'),
    # path('<int:id>/vote/', views.vote, name='vote'),

    path('areaasesoria', catviews.tablaareaasesoria, name='areaasesoria'),
    path('areaasesoria/registro', catviews.registroareaasesoria, name='regareaasesoria'),
    # path('<int:id>/', views.detail, name='detail'),
    # path('<int:id>/results/', views.results, name='results'),
    # path('<int:id>/vote/', views.vote, name='vote'),

    path('tipovisita', catviews.tablatipovisita, name='tipovisita'),
    path('tipovisita/registro', catviews.registrotipovisita, name='regtipovisita'),
    # path('<int:id>/', views.detail, name='detail'),
    # path('<int:id>/results/', views.results, name='results'),
    # path('<int:id>/vote/', views.vote, name='vote'),

    path('enfoque', catviews.tablaenfoque, name='enfoque'),
    path('enfoque/registro', catviews.registroenfoque, name='regenfoque'),
    # path('<int:id>/', views.detail, name='detail'),
    # path('<int:id>/results/', views.results, name='results'),
    # path('<int:id>/vote/', views.vote, name='vote'),

]