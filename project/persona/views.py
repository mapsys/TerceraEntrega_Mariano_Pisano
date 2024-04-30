from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from . import models, forms


def home(request): 
    consulta_personas = models.Usuario.objects.all()
    context = {"usuarios": consulta_personas}
    return render(request, "persona/index.html", context)

# CRUD de Rol
class RolList(ListView):
    model = models.Rol
    # context_object_name = "productos"
    # template_name = "producto/productocategoria___list.html"

class RolCreate(CreateView):
    model = models.Rol
    form_class = forms.RolForm
    success_url = reverse_lazy("persona:rol_list")

class RolUpdate(UpdateView):
    model = models.Rol
    form_class = forms.RolForm
    success_url = reverse_lazy("persona:rol_list")

class RolDetail(DetailView):
    model = models.Rol
    # context_object_name = "producto"

class RolDelete(DeleteView):
    model = models.Rol
    # template_name = "producto/productocategoria_delete.html"
    success_url = reverse_lazy("persona:rol_list")

# CRUD de Usuarios
class UsuarioList(ListView):
    model = models.Usuario
    # context_object_name = "productos"
    # template_name = "producto/productocategoria___list.html"

class UsuarioCreate(CreateView):
    model = models.Usuario
    form_class = forms.UsuarioForm
    success_url = reverse_lazy("persona:usuario_list")

class UsuarioUpdate(UpdateView):
    model = models.Usuario
    form_class = forms.UsuarioForm
    success_url = reverse_lazy("persona:usuario_list")

class UsuarioDetail(DetailView):
    model = models.Usuario
    # context_object_name = "producto"

class UsuarioDelete(DeleteView):
    model = models.Usuario
    # template_name = "producto/productocategoria_delete.html"
    success_url = reverse_lazy("persona:usuario_list")


# CRUD de Clientes
class ClienteList(ListView):
    model = models.Cliente
    # context_object_name = "productos"
    # template_name = "producto/productocategoria___list.html"

class ClienteCreate(CreateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("persona:cliente_list")

class ClienteUpdate(UpdateView):
    model = models.Cliente
    form_class = forms.ClienteForm
    success_url = reverse_lazy("persona:cliente_list")

class ClienteDetail(DetailView):
    model = models.Cliente
    # context_object_name = "producto"

class ClienteDelete(DeleteView):
    model = models.Cliente
    # template_name = "producto/productocategoria_delete.html"
    success_url = reverse_lazy("persona:cliente_list")

