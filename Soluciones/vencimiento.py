__author__ = 'IgnacioTamara'
from Soluciones.models import libros, soluciones, paquetes,tematicas,UsuarioPaq,QRPago
import datetime as fecha

def vencimiento():
    QActivos= UsuarioPaq.objects.select_related().filter(activo=True)

    for h in QActivos:
        fechaVence=h.fechaPago+fecha.timedelta(days=h.paqueteMio.paqueteDias)
        if fechaVence<fecha.date.today():
            UsuarioPaq.objects.filter(id=h.id).update(vencido=True,activo=False)
            print('dggdgdg')
            input()


hilo=0
vencimiento()