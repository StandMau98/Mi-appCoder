from django.http import HttpResponse
from MTV.models import Familia
from django.template import Template, Context, loader

# Create your views here.
def Mi_familia(request):
    conocidos = Familia.objects.all()
    datos = {"Mi_familia": conocidos}
    plantilla = loader.get_template("Familiares.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)


