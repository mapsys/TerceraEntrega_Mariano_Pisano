from django.urls import path

app_name = "persona"

from . import views

urlpatterns = [
    # path("home/", views.home),
    path("", views.home, name="home"),
]
