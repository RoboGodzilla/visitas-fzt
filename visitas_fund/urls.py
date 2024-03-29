"""visitas_fund URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from visita import views as visita_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', visita_views.home, name='home'),
    path('visita', visita_views.tablavisita, name='visita'),
    path('visita/registro', visita_views.registrovisita, name='registro'),
    path('data/', include('visita.urls')),
    path('catalogo/', include('catalogo.urls')),
    path('user/', include('seguridad.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
