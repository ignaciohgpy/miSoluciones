from django.contrib import admin
from Soluciones.models import correoValidacion, libros, soluciones, solucionadores, tematicas,paquetes,UsuarioPaq, QRPago,perfil,ProblemaPaq, comentarios
admin.site.register(libros)
admin.site.register(soluciones)
admin.site.register(solucionadores)
admin.site.register(tematicas)
admin.site.register(paquetes)
admin.site.register(UsuarioPaq)
admin.site.register(QRPago)
admin.site.register(perfil)
admin.site.register(ProblemaPaq)
admin.site.register(comentarios)
admin.site.register(correoValidacion)
# Register your models here.
