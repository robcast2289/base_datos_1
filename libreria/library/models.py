from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TipoUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self) -> str:
        txt = "{0}"
        return txt.format(self.nombre)


class Usuario(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=8)
    tipo = models.ForeignKey(TipoUsuario,null=False,blank=False,on_delete=models.RESTRICT)

    class Meta:
        db_table_comment = "Complemento usuario"

class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        txt = "{0}"
        return txt.format(self.nombre)
    
    class Meta:
        verbose_name_plural = "Autores"

class Editorial(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self) -> str:
        txt = "{0}"
        return txt.format(self.nombre)
    
    class Meta:
        verbose_name_plural = "Editoriales"

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    autor = models.ForeignKey(Autor,null=True,blank=True,on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial,null=True,blank=True,on_delete=models.CASCADE)
    ejemplares = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='library/images',null=True)

    def __str__(self) -> str:
        txt = "{0}"
        return txt.format(self.titulo)


class Pretamo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,null=False,blank=False,on_delete=models.RESTRICT)
    libro = models.ForeignKey(Libro,null=False,blank=False,on_delete=models.RESTRICT)
    fecha_prestamo = models.DateTimeField(blank=False)
    fecha_devolucion = models.DateTimeField(blank=False)
    fecha_devolucion_real = models.DateTimeField(null=True,blank=True)

    class Meta:
        verbose_name = "Prestamo"