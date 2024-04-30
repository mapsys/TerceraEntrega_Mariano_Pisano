from django import forms

from . import models

# class ProductoCategoriaForm(forms.Form):
#     nombre = forms.CharField()
#     descripcion = forms.CharField()


class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.TextInput(attrs={"class": "form-control"}),
            "stock": forms.TextInput(attrs={"class": "form-control"}),
            "precio": forms.TextInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-control"}),
        }
