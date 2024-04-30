from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from . import models


def home(request): 
    consulta_personas = models.Usuario.objects.all()
    context = {"usuarios": consulta_personas}
    return render(request, "persona/index.html", context)

# CRUD de Rol
class RolList(ListView):
    model = models.Rol
    # context_object_name = "productos"
    # template_name = "producto/productocategoria___list.html"


# CRUD de Usuarios
class UsuarioList(ListView):
    model = models.Usuario
    # context_object_name = "productos"
    # template_name = "producto/productocategoria___list.html"

class ClienteList(ListView):
    model = models.Cliente
    # context_object_name = "productos"
    # template_name = "producto/productocategoria___list.html"