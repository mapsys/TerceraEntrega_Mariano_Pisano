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
            "nombre": forms.TextInput(attrs={"class": "form-control", "style": "width: 300px;"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control", "style": "width: 600px;"}),
        }

class UsuarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        
        # Filtra los roles activos y donde el nombre del rol sea diferente a "Cliente@"
        self.fields['rol'].queryset = models.Rol.objects.exclude(nombre="Cliente")

    class Meta:
        model = models.Usuario
        fields = "__all__"
        widgets = {
            "user": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "apellido": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "rol": forms.Select(attrs={"class": "form-control", "style": "width: 300px;"}),
        }

class ClienteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        # Define el valor fijo para el campo 'rol'
        self.fields['rol'].queryset = models.Rol.objects.filter(nombre="Cliente")
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
