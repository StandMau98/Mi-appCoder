"""PROYECTOCODER URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from PROYECTOCODER.views import vista_saludo
from PROYECTOCODER.views import dia_hoy
from PROYECTOCODER.views import nacimiento
from PROYECTOCODER.views import vista_plantilla
from PROYECTOCODER.views import vista_alumnos
from PROYECTOCODER.views import vista_alumnos2

urlpatterns = [
    path('admin/', admin.site.urls),
    path("saludo/", vista_saludo),
    path("Hoy/<nombre>/", dia_hoy),
    path("Nacimiento/<edad>/", nacimiento),
    path("Inicio/", vista_alumnos),
    path("Home/", vista_alumnos2)
]