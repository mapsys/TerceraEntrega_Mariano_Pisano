from django.urls import path

app_name = "persona"

from . import views

urlpatterns = [
    # path("home/", views.home),
    path("", views.home, name="home"),
        # URLs de Roles
    path("rol/list/", views.RolList.as_view(), name="rol_list"),
    path("rol/detail/<int:pk>", views.RolDetail.as_view(), name="rol_detail"),
    path("rol/update/<int:pk>", views.RolUpdate.as_view(), name="rol_update"),
    path("rol/delete/<int:pk>", views.RolDelete.as_view(), name="rol_delete"),
    path("rol/create/", views.RolCreate.as_view(), name="rol_create"),
    # URLs de usuarios
    path("usuario/list/", views.UsuarioList.as_view(), name="usuario_list"),
    path("usuario/detail/<str:pk>", views.UsuarioDetail.as_view(), name="usuario_detail"),
    path("usuario/update/<str:pk>", views.UsuarioUpdate.as_view(), name="usuario_update"),
    path("usuario/delete/<str:pk>", views.UsuarioDelete.as_view(), name="usuario_delete"),
    path("usuario/create/", views.UsuarioCreate.as_view(), name="usuario_create"),
    # URLs de CLientes
    path("cliente/list/", views.ClienteList.as_view(), name="cliente_list"),
    # path("cliente/detail/<int:pk>", views.cliente_detail, name="cliente_detail"),
    # path("cliente/update/<int:pk>", views.cliente_update, name="cliente_update"),
    # path("cliente/delete/<int:pk>", views.cliente_delete, name="cliente_delete"),
    # path("cliente/create/", views.cliente_create, name="cliente_create"),
]
