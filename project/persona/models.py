from django.db import models

# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=50, verbose_name="Descripción", null=True, blank=True)

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Roles"
    
class Usuario(models.Model):
    user = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"user : {self.user}. {self.apellido} , {self.nombre}. ROL = {self.rol}"
    
class Cliente(Usuario):
    puntuacion = models.IntegerField(null=True, blank=True)
    credito = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return super().__str__() + f". CREDITO = {self.credito}. PUNTUACIÓN = {self.puntuacion}"


    
