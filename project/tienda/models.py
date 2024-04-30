from django.db import models
from persona import models as modelPersona

# Create your models here.
class Categoria(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=50, verbose_name="Descripción", null=True, blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Producto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.codigo} - {self.nombre} - {self.precio} - {self.categoria}"
    def __repr__(self):
        return f"{self.codigo} - {self.nombre} - {self.precio} - {self.categoria}"
    
class Carrito(models.Model):
    cliente = models.ForeignKey(modelPersona.Cliente, on_delete=models.CASCADE)
    fecha = models.DateField()
    total = models.IntegerField(null=True, blank=True)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        return f"Cliente: {self.cliente.nombre}, {self.cliente.apellido} - Total: {self.total}"