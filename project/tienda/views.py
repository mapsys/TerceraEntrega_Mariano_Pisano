from django.shortcuts import render, redirect

from . import models, forms


def home(request): 
    consulta_productos = models.Producto.objects.all()
    context = {"productos": consulta_productos}
    return render(request, "tienda/index.html", context)









# SECCION DE CRUD DE CATEGORIAS DE PRODUCTOS
def productocategoria_list(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        print(consulta)
        query = models.Categoria.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Categoria.objects.all()
    context = {"categorias": query}
    return render(request, "tienda/productocategoria_list.html", context)

def productocategoria_create(request):
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("tienda:productocategoria_list")
    else:  # request.method == "GET"
        form = forms.ProductoCategoriaForm()
    return render(request, "tienda/productocategoria_create.html", context={"form": form})

def productocategoria_detail(request, pk: int):
    query = models.Categoria.objects.get(codigo=pk)
    return render(request, "tienda/productocategoria_detail.html", {"categoria": query})

def productocategoria_update(request, pk: int):
    query = models.Categoria.objects.get(codigo=pk)
    if request.method == "POST":
        form = forms.ProductoCategoriaForm(request.POST, instance=query)
        if form.is_valid:
            form.save()
            return redirect("tienda:productocategoria_list")
    else:  # request.method == "GET"
        form = forms.ProductoCategoriaForm(instance=query)
    return render(request, "tienda/productocategoria_update.html", context={"form": form})

def productocategoria_delete(request, pk: int):
    query = models.Categoria.objects.get(codigo=pk)
    if request.method == "POST":
        query.delete()
        return redirect("tienda:productocategoria_list")
    return render(request, "tienda/productocategoria_delete.html", context={"categoria": query})



# SECCION DE CRUD DE PRODUCTOS

def producto_list(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        print(consulta)
        query = models.Producto.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Producto.objects.all()
    context = {"productos": query}
    return render(request, "tienda/producto_list.html", context)

def producto_create(request):
    if request.method == "POST":
        form = forms.ProductoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("tienda:producto_list")
    else:  # request.method == "GET"
        form = forms.ProductoForm()
    return render(request, "tienda/producto_create.html", context={"form": form})

def producto_detail(request, pk: int):
    query = models.Producto.objects.get(codigo=pk)
    return render(request, "tienda/producto_detail.html", {"producto": query})

def producto_update(request, pk: int):
    query = models.Producto.objects.get(codigo=pk)
    if request.method == "POST":
        form = forms.ProductoForm(request.POST, instance=query)
        if form.is_valid:
            form.save()
            return redirect("tienda:producto_list")
    else:  # request.method == "GET"
        form = forms.ProductoForm(instance=query)
    return render(request, "tienda/producto_update.html", context={"form": form})

def producto_delete(request, pk: int):
    query = models.Producto.objects.get(codigo=pk)
    if request.method == "POST":
        query.delete()
        return redirect("tienda:producto_list")
    return render(request, "tienda/producto_delete.html", context={"producto": query})


# SECCION DE CRUD DE CARRITOS
def carrito_list(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        print(consulta)
        query = models.Carrito.objects.filter(nombre__icontains=consulta)
    else:
        query = models.Carrito.objects.all()
    context = {"carritos": query}
    return render(request, "tienda/carrito_list.html", context)

def carrito_create(request):
    if request.method == "POST":
        form = forms.CarritoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("tienda:carrito_list")
    else:  # request.method == "GET"
        form = forms.CarritoForm()
    return render(request, "tienda/carrito_create.html", context={"form": form})

def carrito_detail(request, pk: int):
    query = models.Carrito.objects.get(id=pk)
    return render(request, "tienda/carrito_detail.html", {"carrito": query})

def carrito_update(request, pk: int):
    query = models.Carrito.objects.get(id=pk)
    if request.method == "POST":
        form = forms.CarritoForm(request.POST, instance=query)
        if form.is_valid:
            form.save()
            return redirect("tienda:carrito_list")
    else:  # request.method == "GET"
        form = forms.CarritoForm(instance=query)
    return render(request, "tienda/carrito_update.html", context={"form": form})

def carrito_delete(request, pk: int):
    query = models.Producto.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("tienda:carrito_list")
    return render(request, "tienda/carrito_delete.html", context={"carrito": query})