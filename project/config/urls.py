from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),
    path("persona/", include("persona.urls")),
    path("tienda/", include("tienda.urls")),
]
