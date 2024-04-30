from django import forms

from . import models

# class ProductoCategoriaForm(forms.Form):
#     nombre = forms.CharField()
#     descripcion = forms.CharField()


class RolForm(forms.ModelForm):
    class Meta:
        model = models.Rol
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = "__all__"
        widgets = {
            "user": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "rol": forms.Select(attrs={"class": "form-control"}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = "__all__"
        widgets = {
             "user": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "rol": forms.Select(attrs={"class": "form-control"}),
            "puntuacion": forms.TextInput(attrs={"class": "form-control"}),
            "credito": forms.TextInput(attrs={"class": "form-control"}),
        }
