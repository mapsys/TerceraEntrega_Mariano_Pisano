from django.urls import path

app_name = "tienda"

from . import views

urlpatterns = [
    # path("home/", views.home),
    path("", views.home, name="home"),
    # URLs de Categorias
    path("productocategoria/list/", views.productocategoria_list, name="productocategoria_list"),
    path("productocategoria/detail/<int:pk>", views.productocategoria_detail, name="productocategoria_detail"),
    path("productocategoria/update/<int:pk>", views.productocategoria_update, name="productocategoria_update"),
    path("productocategoria/delete/<int:pk>", views.productocategoria_delete, name="productocategoria_delete"),
    path("productocategoria/create/", views.productocategoria_create, name="productocategoria_create"),
    # URLs de productos
    path("producto/list/", views.producto_list, name="producto_list"),
    path("producto/detail/<int:pk>", views.producto_detail, name="producto_detail"),
    path("producto/update/<int:pk>", views.producto_update, name="producto_update"),
    path("producto/delete/<int:pk>", views.producto_delete, name="producto_delete"),
    path("producto/create/", views.producto_create, name="producto_create"),
    # URLs de Carritos
    path("carrito/list/", views.carrito_list, name="carrito_list"),
]
