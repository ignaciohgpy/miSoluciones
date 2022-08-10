from django.db import models
from django.contrib.auth.models import User

class perfil(models.Model):
    perfilID=models.AutoField(primary_key=True)
    nombrePerfil=models.CharField(max_length = 50)
    def __str__(self):
        return '%s'%(self.nombrePerfil)

class tematicas(models.Model):
    temaNombre=models.CharField(max_length=50, null=True,verbose_name='Nombre del Tema')
    perfilId=models.ForeignKey(perfil,on_delete=models.CASCADE,null=True,verbose_name='Perfil')
    agregadoPor = models.IntegerField(null=True)
    def __str__(self):
        return '%s'%(self.temaNombre)

class libros(models.Model):

    titulo=models.CharField(max_length = 50,null=True,verbose_name="Título" )
    autor=models.CharField(max_length = 50,null=True,verbose_name="Autor" )
    edicion=models.CharField(max_length = 50,null=True,verbose_name="Edición" )
    perfilId=models.ForeignKey(perfil,on_delete=models.CASCADE,null=True,verbose_name="Perfil" )
    def __str__(self):
        return self.titulo
class correoValidacion(models.Model):
    correo=models.EmailField()
    codigo=models.IntegerField()
    validado=models.BooleanField()

class comentarios(models.Model):
    comentario=models.TextField(max_length = 50)
    correo=models.EmailField()
    tipo=models.CharField(max_length = 50)
    usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    nombre=models.CharField(null=True,max_length = 50)
    respuesta=models.TextField(null=True,max_length = 150)
    responsable=models.IntegerField(null=True)
class solucionadores(models.Model):
    solucionadorNombre=models.CharField(max_length = 50)
    solucionadorPais=models.CharField(max_length = 50)
    solucionadorID=models.AutoField(primary_key=True)
    solucionadorPais=models.CharField(null=True,max_length = 50)
    def __str__(self):
        return self.solucionadorNombre

class paquetes(models.Model):
    paqueteID=models.AutoField(primary_key=True)
    paqueteCod=models.CharField(max_length=50, null=True,verbose_name="Codigo del paquete")
    paqueteCant=models.IntegerField(null=True, verbose_name="Cantidad de problemas que contiene")
    paquetePrecio=models.IntegerField(null=True,verbose_name="Precio")
    paqueteDias=models.IntegerField(null=True,verbose_name="Dias que estará activo")
    paqueteDescr=models.CharField(max_length=50, null=True,verbose_name="Descripción")
    paquetePerfil=models.ForeignKey(perfil, on_delete=models.CASCADE,null=True,verbose_name="Perfil")
    paqueteFecha=models.DateField(auto_now_add=True,null=True)
    paqueteCreador=models.ForeignKey(User, on_delete=models.CASCADE,null=True)


    def __str__(self):
        return '%s'%(self.paqueteCod)

class soluciones(models.Model):
    problemaNumero=models.CharField(max_length=50, null=True,verbose_name="Numero del Problema")
    problemaProblema=models.ImageField(upload_to='problemas', null=True,verbose_name="Figura del problema")
    problemaID=models.AutoField(primary_key=True)
    problemaLibro=models.ForeignKey(libros, on_delete=models.CASCADE,null=True,verbose_name="Libro o Guia")
    problemaSolucion=models.FileField(upload_to='soluciones',null=True,verbose_name="Documento de solución")
    problemaVideo=models.FileField(upload_to='videos',null=True,verbose_name="Audio de explicación")
    problemaSolucionadoPor=models.ForeignKey(solucionadores, on_delete=models.CASCADE,null=True,verbose_name="Solucionado por")
    problemaTema=models.ForeignKey(tematicas, on_delete=models.CASCADE,null=True,verbose_name="Tema del problema")
    problemaFecha=models.DateField(auto_now_add=True,)
    def __str__(self):
        return '%s%s'%(self.problemaNumero,self.problemaProblema)

class UsuarioPaq(models.Model):
    usuario=models.IntegerField(null=True)
    fechaIni=models.DateField(blank=True, null=True)
    fechaPago=models.DateField(blank=True, null=True)
    paqueteMio=models.ForeignKey(paquetes,on_delete=models.CASCADE,null=True)
    activo=models.BooleanField(blank=True, null=True)
    vencido=models.BooleanField(blank=True, null=True,default=False)
    def __str__(self):
        return '%s%s'%(self.usuario,self.paqueteMio)

class ProblemaPaq(models.Model):
    problemaID= models.ForeignKey(soluciones,on_delete=models.CASCADE,null=True)
    paqueteID= models.ForeignKey(paquetes,on_delete=models.CASCADE,null=True)

class QRPago(models.Model):
    qr=models.ImageField(upload_to='qr', null=True)
    Nombre=models.CharField(max_length=50, null=True)
    foto=models.ImageField(upload_to='foto', null=True,blank=True)
    

	
