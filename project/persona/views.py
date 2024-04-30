from django.shortcuts import render

from . import models


def home(request): 
    consulta_personas = models.Usuario.objects.all()
    context = {"usuarios": consulta_personas}
    return render(request, "persona/index.html", context)
